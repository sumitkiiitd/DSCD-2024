# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mapper.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_messages_pb2 as common__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmapper.proto\x12\tMapReduce\x1a\x15\x63ommon_messages.proto\"\x8c\x01\n\rDoMapTaskArgs\x12\x0e\n\x06map_id\x18\x01 \x01(\x05\x12\x11\n\tstart_idx\x18\x02 \x01(\x05\x12\x0f\n\x07\x65nd_idx\x18\x03 \x01(\x05\x12\x10\n\x08n_reduce\x18\x04 \x01(\x05\x12#\n\tcentroids\x18\x05 \x03(\x0b\x32\x10.MapReduce.Point\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\"2\n\x0e\x44oMapTaskReply\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x11\n\tworker_id\x18\x02 \x01(\x05\"\x1d\n\x0bGetDataArgs\x12\x0e\n\x06red_id\x18\x01 \x01(\x05\" \n\x0cGetDataReply\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t2\x8a\x01\n\x0eMapperServices\x12<\n\x05\x44oMap\x12\x18.MapReduce.DoMapTaskArgs\x1a\x19.MapReduce.DoMapTaskReply\x12:\n\x07GetData\x12\x16.MapReduce.GetDataArgs\x1a\x17.MapReduce.GetDataReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mapper_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DOMAPTASKARGS']._serialized_start=51
  _globals['_DOMAPTASKARGS']._serialized_end=191
  _globals['_DOMAPTASKREPLY']._serialized_start=193
  _globals['_DOMAPTASKREPLY']._serialized_end=243
  _globals['_GETDATAARGS']._serialized_start=245
  _globals['_GETDATAARGS']._serialized_end=274
  _globals['_GETDATAREPLY']._serialized_start=276
  _globals['_GETDATAREPLY']._serialized_end=308
  _globals['_MAPPERSERVICES']._serialized_start=311
  _globals['_MAPPERSERVICES']._serialized_end=449
# @@protoc_insertion_point(module_scope)
