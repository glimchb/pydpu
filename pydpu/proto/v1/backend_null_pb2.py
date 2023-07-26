# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend_null.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
import object_key_pb2 as object__key__pb2
import opicommon_pb2 as opicommon__pb2
import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62\x61\x63kend_null.proto\x12\x12opi_api.storage.v1\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\x1a\x10object_key.proto\x1a\x0fopicommon.proto\x1a\nuuid.proto\"\xa5\x01\n\nNullVolume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nblock_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x62locks_count\x18\x03 \x01(\x03\x12%\n\x04uuid\x18\x04 \x01(\x0b\x32\x17.opi_api.common.v1.Uuid:8\xea\x41\x35\n!storage.opiproject.org/NullVolume\x12\x10volumes/{volume}\"k\n\x17\x43reateNullVolumeRequest\x12\x38\n\x0bnull_volume\x18\x02 \x01(\x0b\x32\x1e.opi_api.storage.v1.NullVolumeB\x03\xe0\x41\x02\x12\x16\n\x0enull_volume_id\x18\x03 \x01(\t\"e\n\x17\x44\x65leteNullVolumeRequest\x12\x33\n\x04name\x18\x01 \x01(\tB%\xe0\x41\x02\xfa\x41\x1f\n\x1dopi_api.storage.v1/NullVolume\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\"\x96\x01\n\x17UpdateNullVolumeRequest\x12\x33\n\x0bnull_volume\x18\x01 \x01(\x0b\x32\x1e.opi_api.storage.v1.NullVolume\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08\"v\n\x16ListNullVolumesRequest\x12\x35\n\x06parent\x18\x01 \x01(\tB%\xe0\x41\x02\xfa\x41\x1f\n\x1dopi_api.storage.v1/NullVolume\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"h\n\x17ListNullVolumesResponse\x12\x34\n\x0cnull_volumes\x18\x01 \x03(\x0b\x32\x1e.opi_api.storage.v1.NullVolume\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"K\n\x14GetNullVolumeRequest\x12\x33\n\x04name\x18\x01 \x01(\tB%\xe0\x41\x02\xfa\x41\x1f\n\x1dopi_api.storage.v1/NullVolume\"F\n\x16NullVolumeStatsRequest\x12,\n\x06handle\x18\x01 \x01(\x0b\x32\x1c.opi_api.common.v1.ObjectKey\"w\n\x17NullVolumeStatsResponse\x12,\n\x06handle\x18\x01 \x01(\x0b\x32\x1c.opi_api.common.v1.ObjectKey\x12.\n\x05stats\x18\x02 \x01(\x0b\x32\x1f.opi_api.storage.v1.VolumeStats2\x87\x07\n\x11NullVolumeService\x12\x9e\x01\n\x10\x43reateNullVolume\x12+.opi_api.storage.v1.CreateNullVolumeRequest\x1a\x1e.opi_api.storage.v1.NullVolume\"=\x82\xd3\xe4\x93\x02\x1a\"\x0b/v1/volumes:\x0bnull_volume\xda\x41\x1anull_volume,null_volume_id\x12\x89\x01\n\x10\x44\x65leteNullVolume\x12+.opi_api.storage.v1.DeleteNullVolumeRequest\x1a\x16.google.protobuf.Empty\"0\x82\xd3\xe4\x93\x02#*!/v1/{name=subsystems}/{subsystem}\xda\x41\x04name\x12\xb1\x01\n\x10UpdateNullVolume\x12+.opi_api.storage.v1.UpdateNullVolumeRequest\x1a\x1e.opi_api.storage.v1.NullVolume\"P\x82\xd3\xe4\x93\x02\x30\x32!/v1/{null_volume.name=subsystems}:\x0bnull_volume\xda\x41\x17null_volume,update_mask\x12\x94\x01\n\x0fListNullVolumes\x12*.opi_api.storage.v1.ListNullVolumesRequest\x1a+.opi_api.storage.v1.ListNullVolumesResponse\"(\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/{parent=subsystems}\xda\x41\x06parent\x12\x8b\x01\n\rGetNullVolume\x12(.opi_api.storage.v1.GetNullVolumeRequest\x1a\x1e.opi_api.storage.v1.NullVolume\"0\x82\xd3\xe4\x93\x02#\x12!/v1/{name=subsystems}/{subsystem}\xda\x41\x04name\x12l\n\x0fNullVolumeStats\x12*.opi_api.storage.v1.NullVolumeStatsRequest\x1a+.opi_api.storage.v1.NullVolumeStatsResponse\"\x00\x42_\n\x12opi_api.storage.v1B\x10\x42\x61\x63kendNullProtoP\x01Z5github.com/opiproject/opi-api/storage/v1alpha1/gen/gob\x06proto3')



_NULLVOLUME = DESCRIPTOR.message_types_by_name['NullVolume']
_CREATENULLVOLUMEREQUEST = DESCRIPTOR.message_types_by_name['CreateNullVolumeRequest']
_DELETENULLVOLUMEREQUEST = DESCRIPTOR.message_types_by_name['DeleteNullVolumeRequest']
_UPDATENULLVOLUMEREQUEST = DESCRIPTOR.message_types_by_name['UpdateNullVolumeRequest']
_LISTNULLVOLUMESREQUEST = DESCRIPTOR.message_types_by_name['ListNullVolumesRequest']
_LISTNULLVOLUMESRESPONSE = DESCRIPTOR.message_types_by_name['ListNullVolumesResponse']
_GETNULLVOLUMEREQUEST = DESCRIPTOR.message_types_by_name['GetNullVolumeRequest']
_NULLVOLUMESTATSREQUEST = DESCRIPTOR.message_types_by_name['NullVolumeStatsRequest']
_NULLVOLUMESTATSRESPONSE = DESCRIPTOR.message_types_by_name['NullVolumeStatsResponse']
NullVolume = _reflection.GeneratedProtocolMessageType('NullVolume', (_message.Message,), {
  'DESCRIPTOR' : _NULLVOLUME,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.NullVolume)
  })
_sym_db.RegisterMessage(NullVolume)

CreateNullVolumeRequest = _reflection.GeneratedProtocolMessageType('CreateNullVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATENULLVOLUMEREQUEST,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.CreateNullVolumeRequest)
  })
_sym_db.RegisterMessage(CreateNullVolumeRequest)

DeleteNullVolumeRequest = _reflection.GeneratedProtocolMessageType('DeleteNullVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETENULLVOLUMEREQUEST,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.DeleteNullVolumeRequest)
  })
_sym_db.RegisterMessage(DeleteNullVolumeRequest)

UpdateNullVolumeRequest = _reflection.GeneratedProtocolMessageType('UpdateNullVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATENULLVOLUMEREQUEST,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.UpdateNullVolumeRequest)
  })
_sym_db.RegisterMessage(UpdateNullVolumeRequest)

ListNullVolumesRequest = _reflection.GeneratedProtocolMessageType('ListNullVolumesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNULLVOLUMESREQUEST,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.ListNullVolumesRequest)
  })
_sym_db.RegisterMessage(ListNullVolumesRequest)

ListNullVolumesResponse = _reflection.GeneratedProtocolMessageType('ListNullVolumesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNULLVOLUMESRESPONSE,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.ListNullVolumesResponse)
  })
_sym_db.RegisterMessage(ListNullVolumesResponse)

GetNullVolumeRequest = _reflection.GeneratedProtocolMessageType('GetNullVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNULLVOLUMEREQUEST,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.GetNullVolumeRequest)
  })
_sym_db.RegisterMessage(GetNullVolumeRequest)

NullVolumeStatsRequest = _reflection.GeneratedProtocolMessageType('NullVolumeStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _NULLVOLUMESTATSREQUEST,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.NullVolumeStatsRequest)
  })
_sym_db.RegisterMessage(NullVolumeStatsRequest)

NullVolumeStatsResponse = _reflection.GeneratedProtocolMessageType('NullVolumeStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _NULLVOLUMESTATSRESPONSE,
  '__module__' : 'backend_null_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.storage.v1.NullVolumeStatsResponse)
  })
_sym_db.RegisterMessage(NullVolumeStatsResponse)

_NULLVOLUMESERVICE = DESCRIPTOR.services_by_name['NullVolumeService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022opi_api.storage.v1B\020BackendNullProtoP\001Z5github.com/opiproject/opi-api/storage/v1alpha1/gen/go'
  _NULLVOLUME._options = None
  _NULLVOLUME._serialized_options = b'\352A5\n!storage.opiproject.org/NullVolume\022\020volumes/{volume}'
  _CREATENULLVOLUMEREQUEST.fields_by_name['null_volume']._options = None
  _CREATENULLVOLUMEREQUEST.fields_by_name['null_volume']._serialized_options = b'\340A\002'
  _DELETENULLVOLUMEREQUEST.fields_by_name['name']._options = None
  _DELETENULLVOLUMEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\037\n\035opi_api.storage.v1/NullVolume'
  _LISTNULLVOLUMESREQUEST.fields_by_name['parent']._options = None
  _LISTNULLVOLUMESREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A\037\n\035opi_api.storage.v1/NullVolume'
  _GETNULLVOLUMEREQUEST.fields_by_name['name']._options = None
  _GETNULLVOLUMEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\037\n\035opi_api.storage.v1/NullVolume'
  _NULLVOLUMESERVICE.methods_by_name['CreateNullVolume']._options = None
  _NULLVOLUMESERVICE.methods_by_name['CreateNullVolume']._serialized_options = b'\202\323\344\223\002\032\"\013/v1/volumes:\013null_volume\332A\032null_volume,null_volume_id'
  _NULLVOLUMESERVICE.methods_by_name['DeleteNullVolume']._options = None
  _NULLVOLUMESERVICE.methods_by_name['DeleteNullVolume']._serialized_options = b'\202\323\344\223\002#*!/v1/{name=subsystems}/{subsystem}\332A\004name'
  _NULLVOLUMESERVICE.methods_by_name['UpdateNullVolume']._options = None
  _NULLVOLUMESERVICE.methods_by_name['UpdateNullVolume']._serialized_options = b'\202\323\344\223\00202!/v1/{null_volume.name=subsystems}:\013null_volume\332A\027null_volume,update_mask'
  _NULLVOLUMESERVICE.methods_by_name['ListNullVolumes']._options = None
  _NULLVOLUMESERVICE.methods_by_name['ListNullVolumes']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/{parent=subsystems}\332A\006parent'
  _NULLVOLUMESERVICE.methods_by_name['GetNullVolume']._options = None
  _NULLVOLUMESERVICE.methods_by_name['GetNullVolume']._serialized_options = b'\202\323\344\223\002#\022!/v1/{name=subsystems}/{subsystem}\332A\004name'
  _NULLVOLUME._serialized_start=268
  _NULLVOLUME._serialized_end=433
  _CREATENULLVOLUMEREQUEST._serialized_start=435
  _CREATENULLVOLUMEREQUEST._serialized_end=542
  _DELETENULLVOLUMEREQUEST._serialized_start=544
  _DELETENULLVOLUMEREQUEST._serialized_end=645
  _UPDATENULLVOLUMEREQUEST._serialized_start=648
  _UPDATENULLVOLUMEREQUEST._serialized_end=798
  _LISTNULLVOLUMESREQUEST._serialized_start=800
  _LISTNULLVOLUMESREQUEST._serialized_end=918
  _LISTNULLVOLUMESRESPONSE._serialized_start=920
  _LISTNULLVOLUMESRESPONSE._serialized_end=1024
  _GETNULLVOLUMEREQUEST._serialized_start=1026
  _GETNULLVOLUMEREQUEST._serialized_end=1101
  _NULLVOLUMESTATSREQUEST._serialized_start=1103
  _NULLVOLUMESTATSREQUEST._serialized_end=1173
  _NULLVOLUMESTATSRESPONSE._serialized_start=1175
  _NULLVOLUMESTATSRESPONSE._serialized_end=1294
  _NULLVOLUMESERVICE._serialized_start=1297
  _NULLVOLUMESERVICE._serialized_end=2200
# @@protoc_insertion_point(module_scope)
