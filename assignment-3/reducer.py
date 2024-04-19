"""
MapReduce Reducer
"""

from collections import OrderedDict
import os
import argparse
import logging
import time
from concurrent import futures
import typing
import grpc
import yaml

import logger

import reducer_pb2
import reducer_pb2_grpc

import mapper_pb2
import mapper_pb2_grpc

import common_messages_pb2

LOGGING_LEVEL = logging.DEBUG
MAX_WORKERS = 2

BASE_DIR = "Data/"
DEFAULT_MAP_GETDATA_TIMEOUT = 30


class ReduceTask:
    """ReduceTask structure"""

    def __init__(self, reduce_id, mapper_address):
        self.reduce_id = reduce_id
        self.mapper_address = mapper_address
        self.map_data = []
        self.keywise_points = OrderedDict()
        self.keywise_mean_centroids = {}

    def __str__(self):
        return f"[{self.reduce_id}:{self.mapper_address}]"

    def format_data_keywise(self) -> None:
        """Stores the data in form [ [<key> : [<value> , <value>, ...]]"""

        for key, value in self.map_data:
            data_point = ((float(value[0][0]), float(value[0][1])), value[1])
            if key not in self.keywise_points:
                self.keywise_points[key] = []
            self.keywise_points[key].append(data_point)

    def find_mean_keywise(self) -> None:
        """Calculates the centroids found by average"""

        for key, values in self.keywise_points.items():
            sum_x = 0.0
            sum_y = 0
            sum_count = 0
            for point, num in values:
                sum_x += point[0]

                sum_y += point[1]

                sum_count += num
            average_x = sum_x / sum_count
            average_y = sum_y / sum_count

            self.keywise_mean_centroids[key] = [(average_x, average_y)]

        logger.DUMP_LOGGER.info(
            "Centroid list for reduce task %s is: %s",
            self.reduce_id,
            self.keywise_mean_centroids,
        )

    def __get_data_from_mapper(
        self, arg: mapper_pb2.GetDataArgs, addr: str
    ) -> typing.List[typing.Tuple[int, typing.Tuple[float, int]]]:
        """Get data from the mappers by calling the GetData RPC"""
        reply = None
        try:
            with grpc.insecure_channel(addr) as channel:
                stub = mapper_pb2_grpc.MapperServicesStub(channel)
                reply = stub.GetData(arg, timeout=DEFAULT_MAP_GETDATA_TIMEOUT)
        except grpc.RpcError as err:
            if err.code() == grpc.StatusCode.UNAVAILABLE:
                logger.DUMP_LOGGER.error(
                    "Error occurred while sending GetData RPC to Node %s. UNAVAILABLE",
                    str(addr),
                )
            elif err.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                logger.DUMP_LOGGER.error(
                    "Error occurred while sending GetData RPC to Node %s. DEADLINE_EXCEEDED",
                    str(addr),
                )
            else:
                logger.DUMP_LOGGER.error(
                    "Error occurred while sending GetData RPC to Node %s. Unknown. Error: %s",
                    str(addr),
                    str(err),
                )

        if reply is None:
            logger.DUMP_LOGGER.error("Mapper not rechable to get data. Exiting")
            # print("Mapper not rechable to get data. Exiting")
            exit(1)
        data = list(
            map(lambda x: (x.key, ((x.point.x, x.point.y), x.value)), reply.entries)
        )
        return data

    def do_reduce_task(self) -> None:
        """Do the reduce task as per the specificatio"""
        logger.DUMP_LOGGER.info("Got a reduce task: %s", str(self))
        # Get data from mapper
        for i in range(len(self.mapper_address)):
            # logger.DUMP_LOGGER.info("Prepare")
            arg = mapper_pb2.GetDataArgs(
                partition_key=self.reduce_id, map_id=i
            )  # serialize request to mapper
            # logger.DUMP_LOGGER.info(arg)
            mapper_data = self.__get_data_from_mapper(arg, self.mapper_address[i])
            self.map_data = self.map_data + mapper_data

        logger.DUMP_LOGGER.info(
            "Reducer Task %s received data from the mappers", str(self.reduce_id)
        )
        self.format_data_keywise()
        self.find_mean_keywise()
        # print(self.keywise_mean_centroids)

        logger.DUMP_LOGGER.info("Reduce task Done. task: %s.", str(self))

    @classmethod
    def from_pb_to_impl_DoReduceTaskArgs(cls, request: reducer_pb2.DoReduceTaskArgs):
        """Converts DoReduceTaskArgs(pb format) to ReduceTask"""
        # print(request.mapper_address)
        # print(type(request.mapper_address))
        # print(request.mapper_address)
        return cls(
            reduce_id=request.reduce_id,
            mapper_address=[str(addr) for addr in request.mapper_address],
        )


class Reducer(reducer_pb2_grpc.ReducerServiceServicer):
    """MapReduce Reducer"""

    def __init__(self, **kwargs) -> None:
        self.worker_id = kwargs["worker_id"]
        self.worker_port = kwargs["worker_port"]
        self.grpc_server = None

    def __serve(self) -> None:
        """Start services"""
        self.grpc_server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
            options=(("grpc.so_reuseport", 0),),
        )
        reducer_pb2_grpc.add_ReducerServiceServicer_to_server(self, self.grpc_server)
        self.grpc_server.add_insecure_port("0.0.0.0" + ":" + str(self.worker_port))
        self.grpc_server.start()
        logger.DUMP_LOGGER.info("started at port %s", self.worker_port)

    def start(self) -> None:
        """Start reducer"""
        self.__serve()

    def stop(self) -> None:
        """Stop"""
        self.grpc_server.stop(1.5).wait()

    def create_reducers_directory(self):
        """Create Reducers directory if not already created"""
        # Create Reducers directory
        data_directory = "Data"
        reducers_directory = os.path.join(data_directory, "Reducers")
        if not os.path.exists(reducers_directory):
            os.makedirs(reducers_directory)
            logger.DUMP_LOGGER.debug(f"Directory '{reducers_directory }' created.")
        else:
            logger.DUMP_LOGGER.debug(
                f"Directory '{reducers_directory }' already exists."
            )

    def DoReduce(
        self, request: reducer_pb2.DoReduceTaskArgs, context
    ) -> reducer_pb2.DoReduceTaskReply:
        """Implement the DoReduce RPC"""
        reduce_task = ReduceTask.from_pb_to_impl_DoReduceTaskArgs(request)
        # logger.DUMP_LOGGER.debug("New Reduce Task created %s", type(reduce_task.mapper_address))
        reduce_task.do_reduce_task()
        # serialize data here
        # data is of the type dictionary with { key: (value1, value2)}
        logger.DUMP_LOGGER.info(
            "reduced data: %s", str(reduce_task.keywise_mean_centroids)
        )
        reply = reducer_pb2.DoReduceTaskReply()
        reply.status = reducer_pb2.Status.SUCCESS  # Set the status to SUCCESS

        for key, value in reduce_task.keywise_mean_centroids.items():
            centroid_msg = reducer_pb2.Centroid()
            centroid_msg.index = key
            centroid_msg.centroid.x = value[0][0]
            centroid_msg.centroid.y = value[0][1]
            reply.updated_centroids.append(centroid_msg)

        return reply


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="MapReduce Reducer",
        epilog="$ python3 reducer.py -I 0",
    )
    parser.add_argument("-I", "--id", help="Worker ID", required=True, type=int)
    args = parser.parse_args()
    with open("config.yaml", "r", encoding="UTF-8") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
        reducers = config["reducers"]
        this_reducers_addr = config["reducers"][args.id]
    logger.set_logger(
        "logs/", f"reducer_{args.id}.txt", f"reducer-{args.id}", LOGGING_LEVEL
    )
    reducer = Reducer(worker_id=args.id, worker_port=this_reducers_addr.split(":")[1])
    reducer.start()

    try:
        time.sleep(86400)  # Sleep for 24 hours or until interrupted
    except KeyboardInterrupt:
        pass
    reducer.stop()
