# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mapper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_messages_pb2 as common__messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mapper.proto',
  package='MapReduce',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cmapper.proto\x12\tMapReduce\x1a\x15\x63ommon_messages.proto\"\x8c\x01\n\rDoMapTaskArgs\x12\x0e\n\x06map_id\x18\x01 \x01(\x05\x12\x11\n\tstart_idx\x18\x02 \x01(\x05\x12\x0f\n\x07\x65nd_idx\x18\x03 \x01(\x05\x12\x10\n\x08n_reduce\x18\x04 \x01(\x05\x12#\n\tcentroids\x18\x05 \x03(\x0b\x32\x10.MapReduce.Point\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\"U\n\x0e\x44oMapTaskReply\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x11\n\tworker_id\x18\x02 \x01(\x05\x12!\n\x06status\x18\x03 \x01(\x0e\x32\x11.MapReduce.Status\"4\n\x0bGetDataArgs\x12\x15\n\rpartition_key\x18\x01 \x01(\x05\x12\x0e\n\x06map_id\x18\x02 \x01(\x05\"5\n\x0cGetDataReply\x12%\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x14.MapReduce.DataEntry\"H\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1f\n\x05point\x18\x02 \x01(\x0b\x32\x10.MapReduce.Point\x12\r\n\x05value\x18\x03 \x01(\x05\x32\x8a\x01\n\x0eMapperServices\x12<\n\x05\x44oMap\x12\x18.MapReduce.DoMapTaskArgs\x1a\x19.MapReduce.DoMapTaskReply\x12:\n\x07GetData\x12\x16.MapReduce.GetDataArgs\x1a\x17.MapReduce.GetDataReplyb\x06proto3')
  ,
  dependencies=[common__messages__pb2.DESCRIPTOR,])




_DOMAPTASKARGS = _descriptor.Descriptor(
  name='DoMapTaskArgs',
  full_name='MapReduce.DoMapTaskArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_id', full_name='MapReduce.DoMapTaskArgs.map_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_idx', full_name='MapReduce.DoMapTaskArgs.start_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_idx', full_name='MapReduce.DoMapTaskArgs.end_idx', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_reduce', full_name='MapReduce.DoMapTaskArgs.n_reduce', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='centroids', full_name='MapReduce.DoMapTaskArgs.centroids', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='MapReduce.DoMapTaskArgs.filename', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=191,
)


_DOMAPTASKREPLY = _descriptor.Descriptor(
  name='DoMapTaskReply',
  full_name='MapReduce.DoMapTaskReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='MapReduce.DoMapTaskReply.files', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='MapReduce.DoMapTaskReply.worker_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='MapReduce.DoMapTaskReply.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=278,
)


_GETDATAARGS = _descriptor.Descriptor(
  name='GetDataArgs',
  full_name='MapReduce.GetDataArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition_key', full_name='MapReduce.GetDataArgs.partition_key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='MapReduce.GetDataArgs.map_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=332,
)


_GETDATAREPLY = _descriptor.Descriptor(
  name='GetDataReply',
  full_name='MapReduce.GetDataReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='MapReduce.GetDataReply.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=387,
)


_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='MapReduce.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MapReduce.DataEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point', full_name='MapReduce.DataEntry.point', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='MapReduce.DataEntry.value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=461,
)

_DOMAPTASKARGS.fields_by_name['centroids'].message_type = common__messages__pb2._POINT
_DOMAPTASKREPLY.fields_by_name['status'].enum_type = common__messages__pb2._STATUS
_GETDATAREPLY.fields_by_name['entries'].message_type = _DATAENTRY
_DATAENTRY.fields_by_name['point'].message_type = common__messages__pb2._POINT
DESCRIPTOR.message_types_by_name['DoMapTaskArgs'] = _DOMAPTASKARGS
DESCRIPTOR.message_types_by_name['DoMapTaskReply'] = _DOMAPTASKREPLY
DESCRIPTOR.message_types_by_name['GetDataArgs'] = _GETDATAARGS
DESCRIPTOR.message_types_by_name['GetDataReply'] = _GETDATAREPLY
DESCRIPTOR.message_types_by_name['DataEntry'] = _DATAENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DoMapTaskArgs = _reflection.GeneratedProtocolMessageType('DoMapTaskArgs', (_message.Message,), dict(
  DESCRIPTOR = _DOMAPTASKARGS,
  __module__ = 'mapper_pb2'
  # @@protoc_insertion_point(class_scope:MapReduce.DoMapTaskArgs)
  ))
_sym_db.RegisterMessage(DoMapTaskArgs)

DoMapTaskReply = _reflection.GeneratedProtocolMessageType('DoMapTaskReply', (_message.Message,), dict(
  DESCRIPTOR = _DOMAPTASKREPLY,
  __module__ = 'mapper_pb2'
  # @@protoc_insertion_point(class_scope:MapReduce.DoMapTaskReply)
  ))
_sym_db.RegisterMessage(DoMapTaskReply)

GetDataArgs = _reflection.GeneratedProtocolMessageType('GetDataArgs', (_message.Message,), dict(
  DESCRIPTOR = _GETDATAARGS,
  __module__ = 'mapper_pb2'
  # @@protoc_insertion_point(class_scope:MapReduce.GetDataArgs)
  ))
_sym_db.RegisterMessage(GetDataArgs)

GetDataReply = _reflection.GeneratedProtocolMessageType('GetDataReply', (_message.Message,), dict(
  DESCRIPTOR = _GETDATAREPLY,
  __module__ = 'mapper_pb2'
  # @@protoc_insertion_point(class_scope:MapReduce.GetDataReply)
  ))
_sym_db.RegisterMessage(GetDataReply)

DataEntry = _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), dict(
  DESCRIPTOR = _DATAENTRY,
  __module__ = 'mapper_pb2'
  # @@protoc_insertion_point(class_scope:MapReduce.DataEntry)
  ))
_sym_db.RegisterMessage(DataEntry)



_MAPPERSERVICES = _descriptor.ServiceDescriptor(
  name='MapperServices',
  full_name='MapReduce.MapperServices',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=464,
  serialized_end=602,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoMap',
    full_name='MapReduce.MapperServices.DoMap',
    index=0,
    containing_service=None,
    input_type=_DOMAPTASKARGS,
    output_type=_DOMAPTASKREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='MapReduce.MapperServices.GetData',
    index=1,
    containing_service=None,
    input_type=_GETDATAARGS,
    output_type=_GETDATAREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAPPERSERVICES)

DESCRIPTOR.services_by_name['MapperServices'] = _MAPPERSERVICES

# @@protoc_insertion_point(module_scope)
