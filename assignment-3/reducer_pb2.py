# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reducer.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rreducer.proto\x12\tMapReduce\"X\n\x10\x44oReduceTaskArgs\x12\r\n\x05query\x18\x01 \x01(\x05\x12\x1c\n\x14partition_files_path\x18\x02 \x03(\t\x12\x17\n\x0foutput_location\x18\x03 \x01(\t\"\x85\x01\n\x11\x44oReduceTaskReply\x12\x33\n\x06status\x18\x01 \x01(\x0e\x32#.MapReduce.DoReduceTaskReply.Status\x12\x18\n\x10output_file_path\x18\x02 \x01(\t\"!\n\x06Status\x12\n\n\x06\x46\x41ILED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x32Y\n\x0eReducerService\x12G\n\x08\x44oReduce\x12\x1b.MapReduce.DoReduceTaskArgs\x1a\x1c.MapReduce.DoReduceTaskReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reducer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DOREDUCETASKARGS']._serialized_start=28
  _globals['_DOREDUCETASKARGS']._serialized_end=116
  _globals['_DOREDUCETASKREPLY']._serialized_start=119
  _globals['_DOREDUCETASKREPLY']._serialized_end=252
  _globals['_DOREDUCETASKREPLY_STATUS']._serialized_start=219
  _globals['_DOREDUCETASKREPLY_STATUS']._serialized_end=252
  _globals['_REDUCERSERVICE']._serialized_start=254
  _globals['_REDUCERSERVICE']._serialized_end=343
# @@protoc_insertion_point(module_scope)
