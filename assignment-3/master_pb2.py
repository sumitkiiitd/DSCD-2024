# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: master.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_messages_pb2 as common__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmaster.proto\x12\tMapReduce\x1a\x15\x63ommon_messages.proto\"%\n\x10SubmitMapJobArgs\x12\x11\n\tworker_id\x18\x01 \x01(\x05\"\x10\n\x0eSubmitMapReply\"(\n\x13SubmitReduceJobArgs\x12\x11\n\tworker_id\x18\x01 \x01(\x05\"\x13\n\x11SubmitReduceReply2\xa9\x01\n\x0eMasterServices\x12\x46\n\x0cSubmitMapJob\x12\x1b.MapReduce.SubmitMapJobArgs\x1a\x19.MapReduce.SubmitMapReply\x12O\n\x0fSubmitReduceJob\x12\x1e.MapReduce.SubmitReduceJobArgs\x1a\x1c.MapReduce.SubmitReduceReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'master_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SUBMITMAPJOBARGS']._serialized_start=50
  _globals['_SUBMITMAPJOBARGS']._serialized_end=87
  _globals['_SUBMITMAPREPLY']._serialized_start=89
  _globals['_SUBMITMAPREPLY']._serialized_end=105
  _globals['_SUBMITREDUCEJOBARGS']._serialized_start=107
  _globals['_SUBMITREDUCEJOBARGS']._serialized_end=147
  _globals['_SUBMITREDUCEREPLY']._serialized_start=149
  _globals['_SUBMITREDUCEREPLY']._serialized_end=168
  _globals['_MASTERSERVICES']._serialized_start=171
  _globals['_MASTERSERVICES']._serialized_end=340
# @@protoc_insertion_point(module_scope)
