# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frontend_virtio_scsi.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opicommon_pb2 as opicommon__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x66rontend_virtio_scsi.proto\x12\x12opi_api.storage.v1\x1a\x0fopicommon.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\"\xd6\x01\n\x10VirtioScsiTarget\x12<\n\x04name\x18\x01 \x01(\tB.\xe0\x41\x03\xe0\x41\x05\xfa\x41%\n#opi_api.storage.v1/VirtioScsiTarget\x12\x15\n\x08max_luns\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01:m\xea\x41j\n\'storage.opiproject.org/VirtioScsiTarget\x12\x1avirtioScsiTargets/{volume}*\x11virtioScsiTargets2\x10virtioScsiTarget\"\xfa\x02\n\x14VirtioScsiController\x12@\n\x04name\x18\x01 \x01(\tB2\xe0\x41\x03\xe0\x41\x05\xfa\x41)\n\'opi_api.storage.v1/VirtioScsiController\x12\x35\n\x07pcie_id\x18\x02 \x01(\x0b\x32\x1f.opi_api.storage.v1.PciEndpointB\x03\xe0\x41\x02\x12\x34\n\tmin_limit\x18\x03 \x01(\x0b\x32\x1c.opi_api.storage.v1.QosLimitB\x03\xe0\x41\x01\x12\x34\n\tmax_limit\x18\x04 \x01(\x0b\x32\x1c.opi_api.storage.v1.QosLimitB\x03\xe0\x41\x01:}\xea\x41z\n+storage.opiproject.org/VirtioScsiController\x12\x1evirtioScsiControllers/{volume}*\x15virtioScsiControllers2\x14virtioScsiController\"\xe9\x01\n\rVirtioScsiLun\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x03\xe0\x41\x05\xfa\x41\"\n opi_api.storage.v1/VirtioScsiLun\x12\x1c\n\x0ftarget_name_ref\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x1c\n\x0fvolume_name_ref\x18\x03 \x01(\tB\x03\xe0\x41\x02:a\xea\x41^\n$storage.opiproject.org/VirtioScsiLun\x12\x17virtioScsiLuns/{volume}*\x0evirtioScsiLuns2\rvirtioScsiLun\"\x8a\x01\n\x1d\x43reateVirtioScsiTargetRequest\x12\x45\n\x12virtio_scsi_target\x18\x01 \x01(\x0b\x32$.opi_api.storage.v1.VirtioScsiTargetB\x03\xe0\x41\x02\x12\"\n\x15virtio_scsi_target_id\x18\x02 \x01(\tB\x03\xe0\x41\x01\"v\n\x1d\x44\x65leteVirtioScsiTargetRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#opi_api.storage.v1/VirtioScsiTarget\x12\x1a\n\rallow_missing\x18\x02 \x01(\x08\x42\x03\xe0\x41\x01\"\xb8\x01\n\x1dUpdateVirtioScsiTargetRequest\x12\x45\n\x12virtio_scsi_target\x18\x01 \x01(\x0b\x32$.opi_api.storage.v1.VirtioScsiTargetB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01\x12\x1a\n\rallow_missing\x18\x03 \x01(\x08\x42\x03\xe0\x41\x01\"\x8c\x01\n\x1cListVirtioScsiTargetsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#opi_api.storage.v1/VirtioScsiTarget\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\"{\n\x1dListVirtioScsiTargetsResponse\x12\x41\n\x13virtio_scsi_targets\x18\x01 \x03(\x0b\x32$.opi_api.storage.v1.VirtioScsiTarget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"W\n\x1aGetVirtioScsiTargetRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#opi_api.storage.v1/VirtioScsiTarget\"Y\n\x1cStatsVirtioScsiTargetRequest\x12\x39\n\x04name\x18\x01 \x01(\tB+\xe0\x41\x02\xfa\x41%\n#opi_api.storage.v1/VirtioScsiTarget\"O\n\x1dStatsVirtioScsiTargetResponse\x12.\n\x05stats\x18\x01 \x01(\x0b\x32\x1f.opi_api.storage.v1.VolumeStats\"\x9a\x01\n!CreateVirtioScsiControllerRequest\x12M\n\x16virtio_scsi_controller\x18\x01 \x01(\x0b\x32(.opi_api.storage.v1.VirtioScsiControllerB\x03\xe0\x41\x02\x12&\n\x19virtio_scsi_controller_id\x18\x02 \x01(\tB\x03\xe0\x41\x01\"~\n!DeleteVirtioScsiControllerRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'opi_api.storage.v1/VirtioScsiController\x12\x1a\n\rallow_missing\x18\x02 \x01(\x08\x42\x03\xe0\x41\x01\"\xc4\x01\n!UpdateVirtioScsiControllerRequest\x12M\n\x16virtio_scsi_controller\x18\x01 \x01(\x0b\x32(.opi_api.storage.v1.VirtioScsiControllerB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01\x12\x1a\n\rallow_missing\x18\x03 \x01(\x08\x42\x03\xe0\x41\x01\"\x94\x01\n ListVirtioScsiControllersRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'opi_api.storage.v1/VirtioScsiController\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\"\x87\x01\n!ListVirtioScsiControllersResponse\x12I\n\x17virtio_scsi_controllers\x18\x01 \x03(\x0b\x32(.opi_api.storage.v1.VirtioScsiController\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"_\n\x1eGetVirtioScsiControllerRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'opi_api.storage.v1/VirtioScsiController\"a\n StatsVirtioScsiControllerRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'opi_api.storage.v1/VirtioScsiController\"S\n!StatsVirtioScsiControllerResponse\x12.\n\x05stats\x18\x01 \x01(\x0b\x32\x1f.opi_api.storage.v1.VolumeStats\"~\n\x1a\x43reateVirtioScsiLunRequest\x12?\n\x0fvirtio_scsi_lun\x18\x01 \x01(\x0b\x32!.opi_api.storage.v1.VirtioScsiLunB\x03\xe0\x41\x02\x12\x1f\n\x12virtio_scsi_lun_id\x18\x02 \x01(\tB\x03\xe0\x41\x01\"p\n\x1a\x44\x65leteVirtioScsiLunRequest\x12\x36\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n opi_api.storage.v1/VirtioScsiLun\x12\x1a\n\rallow_missing\x18\x02 \x01(\x08\x42\x03\xe0\x41\x01\"\xaf\x01\n\x1aUpdateVirtioScsiLunRequest\x12?\n\x0fvirtio_scsi_lun\x18\x01 \x01(\x0b\x32!.opi_api.storage.v1.VirtioScsiLunB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01\x12\x1a\n\rallow_missing\x18\x03 \x01(\x08\x42\x03\xe0\x41\x01\"\x86\x01\n\x19ListVirtioScsiLunsRequest\x12\x38\n\x06parent\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n opi_api.storage.v1/VirtioScsiLun\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\"r\n\x1aListVirtioScsiLunsResponse\x12;\n\x10virtio_scsi_luns\x18\x01 \x03(\x0b\x32!.opi_api.storage.v1.VirtioScsiLun\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"Q\n\x17GetVirtioScsiLunRequest\x12\x36\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n opi_api.storage.v1/VirtioScsiLun\"u\n\x19StatsVirtioScsiLunRequest\x12\x36\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n opi_api.storage.v1/VirtioScsiLun\x12 \n\x13\x63ontroller_name_ref\x18\x02 \x01(\tB\x03\xe0\x41\x01\"L\n\x1aStatsVirtioScsiLunResponse\x12.\n\x05stats\x18\x01 \x01(\x0b\x32\x1f.opi_api.storage.v1.VolumeStats2\x91\x1a\n\x19\x46rontendVirtioScsiService\x12\xcf\x01\n\x16\x43reateVirtioScsiTarget\x12\x31.opi_api.storage.v1.CreateVirtioScsiTargetRequest\x1a$.opi_api.storage.v1.VirtioScsiTarget\"\\\x82\xd3\xe4\x93\x02+\"\x15/v1/virtioScsiTargets:\x12virtio_scsi_target\xda\x41(virtio_scsi_target,virtio_scsi_target_id\x12\x92\x01\n\x16\x44\x65leteVirtioScsiTarget\x12\x31.opi_api.storage.v1.DeleteVirtioScsiTargetRequest\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=virtioScsiTargets/*}\xda\x41\x04name\x12\xe1\x01\n\x16UpdateVirtioScsiTarget\x12\x31.opi_api.storage.v1.UpdateVirtioScsiTargetRequest\x1a$.opi_api.storage.v1.VirtioScsiTarget\"n\x82\xd3\xe4\x93\x02G21/v1/{virtio_scsi_target.name=virtioScsiTargets/*}:\x12virtio_scsi_target\xda\x41\x1evirtio_scsi_target,update_mask\x12\xa6\x01\n\x15ListVirtioScsiTargets\x12\x30.opi_api.storage.v1.ListVirtioScsiTargetsRequest\x1a\x31.opi_api.storage.v1.ListVirtioScsiTargetsResponse\"(\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/{parent=subsystems}\xda\x41\x06parent\x12\x9a\x01\n\x13GetVirtioScsiTarget\x12..opi_api.storage.v1.GetVirtioScsiTargetRequest\x1a$.opi_api.storage.v1.VirtioScsiTarget\"-\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=virtioScsiTargets/*}\xda\x41\x04name\x12\xb1\x01\n\x15StatsVirtioScsiTarget\x12\x30.opi_api.storage.v1.StatsVirtioScsiTargetRequest\x1a\x31.opi_api.storage.v1.StatsVirtioScsiTargetResponse\"3\x82\xd3\xe4\x93\x02&\x12$/v1/{name=virtioScsiTargets/*}:stats\xda\x41\x04name\x12\xeb\x01\n\x1a\x43reateVirtioScsiController\x12\x35.opi_api.storage.v1.CreateVirtioScsiControllerRequest\x1a(.opi_api.storage.v1.VirtioScsiController\"l\x82\xd3\xe4\x93\x02\x33\"\x19/v1/virtioScsiControllers:\x16virtio_scsi_controller\xda\x41\x30virtio_scsi_controller,virtio_scsi_controller_id\x12\x9e\x01\n\x1a\x44\x65leteVirtioScsiController\x12\x35.opi_api.storage.v1.DeleteVirtioScsiControllerRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02$*\"/v1/{name=virtioScsiControllers/*}\xda\x41\x04name\x12\xfd\x01\n\x1aUpdateVirtioScsiController\x12\x35.opi_api.storage.v1.UpdateVirtioScsiControllerRequest\x1a(.opi_api.storage.v1.VirtioScsiController\"~\x82\xd3\xe4\x93\x02S29/v1/{virtio_scsi_controller.name=virtioScsiControllers/*}:\x16virtio_scsi_controller\xda\x41\"virtio_scsi_controller,update_mask\x12\xbd\x01\n\x19ListVirtioScsiControllers\x12\x34.opi_api.storage.v1.ListVirtioScsiControllersRequest\x1a\x35.opi_api.storage.v1.ListVirtioScsiControllersResponse\"3\x82\xd3\xe4\x93\x02$\x12\"/v1/{parent=virtioScsiControllers}\xda\x41\x06parent\x12\xaa\x01\n\x17GetVirtioScsiController\x12\x32.opi_api.storage.v1.GetVirtioScsiControllerRequest\x1a(.opi_api.storage.v1.VirtioScsiController\"1\x82\xd3\xe4\x93\x02$\x12\"/v1/{name=virtioScsiControllers/*}\xda\x41\x04name\x12\xc1\x01\n\x19StatsVirtioScsiController\x12\x34.opi_api.storage.v1.StatsVirtioScsiControllerRequest\x1a\x35.opi_api.storage.v1.StatsVirtioScsiControllerResponse\"7\x82\xd3\xe4\x93\x02*\x12(/v1/{name=virtioScsiControllers/*}:stats\xda\x41\x04name\x12\xba\x01\n\x13\x43reateVirtioScsiLun\x12..opi_api.storage.v1.CreateVirtioScsiLunRequest\x1a!.opi_api.storage.v1.VirtioScsiLun\"P\x82\xd3\xe4\x93\x02%\"\x12/v1/virtioScsiLuns:\x0fvirtio_scsi_lun\xda\x41\"virtio_scsi_lun,virtio_scsi_lun_id\x12\x89\x01\n\x13\x44\x65leteVirtioScsiLun\x12..opi_api.storage.v1.DeleteVirtioScsiLunRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/{name=virtioScsiLuns/*}\xda\x41\x04name\x12\xcc\x01\n\x13UpdateVirtioScsiLun\x12..opi_api.storage.v1.UpdateVirtioScsiLunRequest\x1a!.opi_api.storage.v1.VirtioScsiLun\"b\x82\xd3\xe4\x93\x02>2+/v1/{virtio_scsi_lun.name=virtioScsiLuns/*}:\x0fvirtio_scsi_lun\xda\x41\x1bvirtio_scsi_lun,update_mask\x12\x9d\x01\n\x12ListVirtioScsiLuns\x12-.opi_api.storage.v1.ListVirtioScsiLunsRequest\x1a..opi_api.storage.v1.ListVirtioScsiLunsResponse\"(\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/{parent=subsystems}\xda\x41\x06parent\x12\x8e\x01\n\x10GetVirtioScsiLun\x12+.opi_api.storage.v1.GetVirtioScsiLunRequest\x1a!.opi_api.storage.v1.VirtioScsiLun\"*\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/{name=virtioScsiLuns/*}\xda\x41\x04name\x12\xa5\x01\n\x12StatsVirtioScsiLun\x12-.opi_api.storage.v1.StatsVirtioScsiLunRequest\x1a..opi_api.storage.v1.StatsVirtioScsiLunResponse\"0\x82\xd3\xe4\x93\x02#\x12!/v1/{name=virtioScsiLuns/*}:stats\xda\x41\x04nameBf\n\x12opi_api.storage.v1B\x17\x46rontendVirtioScsiProtoP\x01Z5github.com/opiproject/opi-api/storage/v1alpha1/gen/gob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'frontend_virtio_scsi_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022opi_api.storage.v1B\027FrontendVirtioScsiProtoP\001Z5github.com/opiproject/opi-api/storage/v1alpha1/gen/go'
  _VIRTIOSCSITARGET.fields_by_name['name']._options = None
  _VIRTIOSCSITARGET.fields_by_name['name']._serialized_options = b'\340A\003\340A\005\372A%\n#opi_api.storage.v1/VirtioScsiTarget'
  _VIRTIOSCSITARGET.fields_by_name['max_luns']._options = None
  _VIRTIOSCSITARGET.fields_by_name['max_luns']._serialized_options = b'\340A\001'
  _VIRTIOSCSITARGET._options = None
  _VIRTIOSCSITARGET._serialized_options = b'\352Aj\n\'storage.opiproject.org/VirtioScsiTarget\022\032virtioScsiTargets/{volume}*\021virtioScsiTargets2\020virtioScsiTarget'
  _VIRTIOSCSICONTROLLER.fields_by_name['name']._options = None
  _VIRTIOSCSICONTROLLER.fields_by_name['name']._serialized_options = b'\340A\003\340A\005\372A)\n\'opi_api.storage.v1/VirtioScsiController'
  _VIRTIOSCSICONTROLLER.fields_by_name['pcie_id']._options = None
  _VIRTIOSCSICONTROLLER.fields_by_name['pcie_id']._serialized_options = b'\340A\002'
  _VIRTIOSCSICONTROLLER.fields_by_name['min_limit']._options = None
  _VIRTIOSCSICONTROLLER.fields_by_name['min_limit']._serialized_options = b'\340A\001'
  _VIRTIOSCSICONTROLLER.fields_by_name['max_limit']._options = None
  _VIRTIOSCSICONTROLLER.fields_by_name['max_limit']._serialized_options = b'\340A\001'
  _VIRTIOSCSICONTROLLER._options = None
  _VIRTIOSCSICONTROLLER._serialized_options = b'\352Az\n+storage.opiproject.org/VirtioScsiController\022\036virtioScsiControllers/{volume}*\025virtioScsiControllers2\024virtioScsiController'
  _VIRTIOSCSILUN.fields_by_name['name']._options = None
  _VIRTIOSCSILUN.fields_by_name['name']._serialized_options = b'\340A\003\340A\005\372A\"\n opi_api.storage.v1/VirtioScsiLun'
  _VIRTIOSCSILUN.fields_by_name['target_name_ref']._options = None
  _VIRTIOSCSILUN.fields_by_name['target_name_ref']._serialized_options = b'\340A\002'
  _VIRTIOSCSILUN.fields_by_name['volume_name_ref']._options = None
  _VIRTIOSCSILUN.fields_by_name['volume_name_ref']._serialized_options = b'\340A\002'
  _VIRTIOSCSILUN._options = None
  _VIRTIOSCSILUN._serialized_options = b'\352A^\n$storage.opiproject.org/VirtioScsiLun\022\027virtioScsiLuns/{volume}*\016virtioScsiLuns2\rvirtioScsiLun'
  _CREATEVIRTIOSCSITARGETREQUEST.fields_by_name['virtio_scsi_target']._options = None
  _CREATEVIRTIOSCSITARGETREQUEST.fields_by_name['virtio_scsi_target']._serialized_options = b'\340A\002'
  _CREATEVIRTIOSCSITARGETREQUEST.fields_by_name['virtio_scsi_target_id']._options = None
  _CREATEVIRTIOSCSITARGETREQUEST.fields_by_name['virtio_scsi_target_id']._serialized_options = b'\340A\001'
  _DELETEVIRTIOSCSITARGETREQUEST.fields_by_name['name']._options = None
  _DELETEVIRTIOSCSITARGETREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A%\n#opi_api.storage.v1/VirtioScsiTarget'
  _DELETEVIRTIOSCSITARGETREQUEST.fields_by_name['allow_missing']._options = None
  _DELETEVIRTIOSCSITARGETREQUEST.fields_by_name['allow_missing']._serialized_options = b'\340A\001'
  _UPDATEVIRTIOSCSITARGETREQUEST.fields_by_name['virtio_scsi_target']._options = None
  _UPDATEVIRTIOSCSITARGETREQUEST.fields_by_name['virtio_scsi_target']._serialized_options = b'\340A\002'
  _UPDATEVIRTIOSCSITARGETREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEVIRTIOSCSITARGETREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\001'
  _UPDATEVIRTIOSCSITARGETREQUEST.fields_by_name['allow_missing']._options = None
  _UPDATEVIRTIOSCSITARGETREQUEST.fields_by_name['allow_missing']._serialized_options = b'\340A\001'
  _LISTVIRTIOSCSITARGETSREQUEST.fields_by_name['parent']._options = None
  _LISTVIRTIOSCSITARGETSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A%\n#opi_api.storage.v1/VirtioScsiTarget'
  _LISTVIRTIOSCSITARGETSREQUEST.fields_by_name['page_size']._options = None
  _LISTVIRTIOSCSITARGETSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTVIRTIOSCSITARGETSREQUEST.fields_by_name['page_token']._options = None
  _LISTVIRTIOSCSITARGETSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _GETVIRTIOSCSITARGETREQUEST.fields_by_name['name']._options = None
  _GETVIRTIOSCSITARGETREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A%\n#opi_api.storage.v1/VirtioScsiTarget'
  _STATSVIRTIOSCSITARGETREQUEST.fields_by_name['name']._options = None
  _STATSVIRTIOSCSITARGETREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A%\n#opi_api.storage.v1/VirtioScsiTarget'
  _CREATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['virtio_scsi_controller']._options = None
  _CREATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['virtio_scsi_controller']._serialized_options = b'\340A\002'
  _CREATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['virtio_scsi_controller_id']._options = None
  _CREATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['virtio_scsi_controller_id']._serialized_options = b'\340A\001'
  _DELETEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['name']._options = None
  _DELETEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A)\n\'opi_api.storage.v1/VirtioScsiController'
  _DELETEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['allow_missing']._options = None
  _DELETEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['allow_missing']._serialized_options = b'\340A\001'
  _UPDATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['virtio_scsi_controller']._options = None
  _UPDATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['virtio_scsi_controller']._serialized_options = b'\340A\002'
  _UPDATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\001'
  _UPDATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['allow_missing']._options = None
  _UPDATEVIRTIOSCSICONTROLLERREQUEST.fields_by_name['allow_missing']._serialized_options = b'\340A\001'
  _LISTVIRTIOSCSICONTROLLERSREQUEST.fields_by_name['parent']._options = None
  _LISTVIRTIOSCSICONTROLLERSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A)\n\'opi_api.storage.v1/VirtioScsiController'
  _LISTVIRTIOSCSICONTROLLERSREQUEST.fields_by_name['page_size']._options = None
  _LISTVIRTIOSCSICONTROLLERSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTVIRTIOSCSICONTROLLERSREQUEST.fields_by_name['page_token']._options = None
  _LISTVIRTIOSCSICONTROLLERSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _GETVIRTIOSCSICONTROLLERREQUEST.fields_by_name['name']._options = None
  _GETVIRTIOSCSICONTROLLERREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A)\n\'opi_api.storage.v1/VirtioScsiController'
  _STATSVIRTIOSCSICONTROLLERREQUEST.fields_by_name['name']._options = None
  _STATSVIRTIOSCSICONTROLLERREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A)\n\'opi_api.storage.v1/VirtioScsiController'
  _CREATEVIRTIOSCSILUNREQUEST.fields_by_name['virtio_scsi_lun']._options = None
  _CREATEVIRTIOSCSILUNREQUEST.fields_by_name['virtio_scsi_lun']._serialized_options = b'\340A\002'
  _CREATEVIRTIOSCSILUNREQUEST.fields_by_name['virtio_scsi_lun_id']._options = None
  _CREATEVIRTIOSCSILUNREQUEST.fields_by_name['virtio_scsi_lun_id']._serialized_options = b'\340A\001'
  _DELETEVIRTIOSCSILUNREQUEST.fields_by_name['name']._options = None
  _DELETEVIRTIOSCSILUNREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n opi_api.storage.v1/VirtioScsiLun'
  _DELETEVIRTIOSCSILUNREQUEST.fields_by_name['allow_missing']._options = None
  _DELETEVIRTIOSCSILUNREQUEST.fields_by_name['allow_missing']._serialized_options = b'\340A\001'
  _UPDATEVIRTIOSCSILUNREQUEST.fields_by_name['virtio_scsi_lun']._options = None
  _UPDATEVIRTIOSCSILUNREQUEST.fields_by_name['virtio_scsi_lun']._serialized_options = b'\340A\002'
  _UPDATEVIRTIOSCSILUNREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEVIRTIOSCSILUNREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\001'
  _UPDATEVIRTIOSCSILUNREQUEST.fields_by_name['allow_missing']._options = None
  _UPDATEVIRTIOSCSILUNREQUEST.fields_by_name['allow_missing']._serialized_options = b'\340A\001'
  _LISTVIRTIOSCSILUNSREQUEST.fields_by_name['parent']._options = None
  _LISTVIRTIOSCSILUNSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A\"\n opi_api.storage.v1/VirtioScsiLun'
  _LISTVIRTIOSCSILUNSREQUEST.fields_by_name['page_size']._options = None
  _LISTVIRTIOSCSILUNSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTVIRTIOSCSILUNSREQUEST.fields_by_name['page_token']._options = None
  _LISTVIRTIOSCSILUNSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _GETVIRTIOSCSILUNREQUEST.fields_by_name['name']._options = None
  _GETVIRTIOSCSILUNREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n opi_api.storage.v1/VirtioScsiLun'
  _STATSVIRTIOSCSILUNREQUEST.fields_by_name['name']._options = None
  _STATSVIRTIOSCSILUNREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n opi_api.storage.v1/VirtioScsiLun'
  _STATSVIRTIOSCSILUNREQUEST.fields_by_name['controller_name_ref']._options = None
  _STATSVIRTIOSCSILUNREQUEST.fields_by_name['controller_name_ref']._serialized_options = b'\340A\001'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['CreateVirtioScsiTarget']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['CreateVirtioScsiTarget']._serialized_options = b'\202\323\344\223\002+\"\025/v1/virtioScsiTargets:\022virtio_scsi_target\332A(virtio_scsi_target,virtio_scsi_target_id'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['DeleteVirtioScsiTarget']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['DeleteVirtioScsiTarget']._serialized_options = b'\202\323\344\223\002 *\036/v1/{name=virtioScsiTargets/*}\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['UpdateVirtioScsiTarget']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['UpdateVirtioScsiTarget']._serialized_options = b'\202\323\344\223\002G21/v1/{virtio_scsi_target.name=virtioScsiTargets/*}:\022virtio_scsi_target\332A\036virtio_scsi_target,update_mask'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['ListVirtioScsiTargets']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['ListVirtioScsiTargets']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/{parent=subsystems}\332A\006parent'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['GetVirtioScsiTarget']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['GetVirtioScsiTarget']._serialized_options = b'\202\323\344\223\002 \022\036/v1/{name=virtioScsiTargets/*}\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['StatsVirtioScsiTarget']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['StatsVirtioScsiTarget']._serialized_options = b'\202\323\344\223\002&\022$/v1/{name=virtioScsiTargets/*}:stats\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['CreateVirtioScsiController']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['CreateVirtioScsiController']._serialized_options = b'\202\323\344\223\0023\"\031/v1/virtioScsiControllers:\026virtio_scsi_controller\332A0virtio_scsi_controller,virtio_scsi_controller_id'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['DeleteVirtioScsiController']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['DeleteVirtioScsiController']._serialized_options = b'\202\323\344\223\002$*\"/v1/{name=virtioScsiControllers/*}\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['UpdateVirtioScsiController']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['UpdateVirtioScsiController']._serialized_options = b'\202\323\344\223\002S29/v1/{virtio_scsi_controller.name=virtioScsiControllers/*}:\026virtio_scsi_controller\332A\"virtio_scsi_controller,update_mask'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['ListVirtioScsiControllers']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['ListVirtioScsiControllers']._serialized_options = b'\202\323\344\223\002$\022\"/v1/{parent=virtioScsiControllers}\332A\006parent'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['GetVirtioScsiController']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['GetVirtioScsiController']._serialized_options = b'\202\323\344\223\002$\022\"/v1/{name=virtioScsiControllers/*}\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['StatsVirtioScsiController']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['StatsVirtioScsiController']._serialized_options = b'\202\323\344\223\002*\022(/v1/{name=virtioScsiControllers/*}:stats\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['CreateVirtioScsiLun']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['CreateVirtioScsiLun']._serialized_options = b'\202\323\344\223\002%\"\022/v1/virtioScsiLuns:\017virtio_scsi_lun\332A\"virtio_scsi_lun,virtio_scsi_lun_id'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['DeleteVirtioScsiLun']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['DeleteVirtioScsiLun']._serialized_options = b'\202\323\344\223\002\035*\033/v1/{name=virtioScsiLuns/*}\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['UpdateVirtioScsiLun']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['UpdateVirtioScsiLun']._serialized_options = b'\202\323\344\223\002>2+/v1/{virtio_scsi_lun.name=virtioScsiLuns/*}:\017virtio_scsi_lun\332A\033virtio_scsi_lun,update_mask'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['ListVirtioScsiLuns']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['ListVirtioScsiLuns']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/{parent=subsystems}\332A\006parent'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['GetVirtioScsiLun']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['GetVirtioScsiLun']._serialized_options = b'\202\323\344\223\002\035\022\033/v1/{name=virtioScsiLuns/*}\332A\004name'
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['StatsVirtioScsiLun']._options = None
  _FRONTENDVIRTIOSCSISERVICE.methods_by_name['StatsVirtioScsiLun']._serialized_options = b'\202\323\344\223\002#\022!/v1/{name=virtioScsiLuns/*}:stats\332A\004name'
  _VIRTIOSCSITARGET._serialized_start=246
  _VIRTIOSCSITARGET._serialized_end=460
  _VIRTIOSCSICONTROLLER._serialized_start=463
  _VIRTIOSCSICONTROLLER._serialized_end=841
  _VIRTIOSCSILUN._serialized_start=844
  _VIRTIOSCSILUN._serialized_end=1077
  _CREATEVIRTIOSCSITARGETREQUEST._serialized_start=1080
  _CREATEVIRTIOSCSITARGETREQUEST._serialized_end=1218
  _DELETEVIRTIOSCSITARGETREQUEST._serialized_start=1220
  _DELETEVIRTIOSCSITARGETREQUEST._serialized_end=1338
  _UPDATEVIRTIOSCSITARGETREQUEST._serialized_start=1341
  _UPDATEVIRTIOSCSITARGETREQUEST._serialized_end=1525
  _LISTVIRTIOSCSITARGETSREQUEST._serialized_start=1528
  _LISTVIRTIOSCSITARGETSREQUEST._serialized_end=1668
  _LISTVIRTIOSCSITARGETSRESPONSE._serialized_start=1670
  _LISTVIRTIOSCSITARGETSRESPONSE._serialized_end=1793
  _GETVIRTIOSCSITARGETREQUEST._serialized_start=1795
  _GETVIRTIOSCSITARGETREQUEST._serialized_end=1882
  _STATSVIRTIOSCSITARGETREQUEST._serialized_start=1884
  _STATSVIRTIOSCSITARGETREQUEST._serialized_end=1973
  _STATSVIRTIOSCSITARGETRESPONSE._serialized_start=1975
  _STATSVIRTIOSCSITARGETRESPONSE._serialized_end=2054
  _CREATEVIRTIOSCSICONTROLLERREQUEST._serialized_start=2057
  _CREATEVIRTIOSCSICONTROLLERREQUEST._serialized_end=2211
  _DELETEVIRTIOSCSICONTROLLERREQUEST._serialized_start=2213
  _DELETEVIRTIOSCSICONTROLLERREQUEST._serialized_end=2339
  _UPDATEVIRTIOSCSICONTROLLERREQUEST._serialized_start=2342
  _UPDATEVIRTIOSCSICONTROLLERREQUEST._serialized_end=2538
  _LISTVIRTIOSCSICONTROLLERSREQUEST._serialized_start=2541
  _LISTVIRTIOSCSICONTROLLERSREQUEST._serialized_end=2689
  _LISTVIRTIOSCSICONTROLLERSRESPONSE._serialized_start=2692
  _LISTVIRTIOSCSICONTROLLERSRESPONSE._serialized_end=2827
  _GETVIRTIOSCSICONTROLLERREQUEST._serialized_start=2829
  _GETVIRTIOSCSICONTROLLERREQUEST._serialized_end=2924
  _STATSVIRTIOSCSICONTROLLERREQUEST._serialized_start=2926
  _STATSVIRTIOSCSICONTROLLERREQUEST._serialized_end=3023
  _STATSVIRTIOSCSICONTROLLERRESPONSE._serialized_start=3025
  _STATSVIRTIOSCSICONTROLLERRESPONSE._serialized_end=3108
  _CREATEVIRTIOSCSILUNREQUEST._serialized_start=3110
  _CREATEVIRTIOSCSILUNREQUEST._serialized_end=3236
  _DELETEVIRTIOSCSILUNREQUEST._serialized_start=3238
  _DELETEVIRTIOSCSILUNREQUEST._serialized_end=3350
  _UPDATEVIRTIOSCSILUNREQUEST._serialized_start=3353
  _UPDATEVIRTIOSCSILUNREQUEST._serialized_end=3528
  _LISTVIRTIOSCSILUNSREQUEST._serialized_start=3531
  _LISTVIRTIOSCSILUNSREQUEST._serialized_end=3665
  _LISTVIRTIOSCSILUNSRESPONSE._serialized_start=3667
  _LISTVIRTIOSCSILUNSRESPONSE._serialized_end=3781
  _GETVIRTIOSCSILUNREQUEST._serialized_start=3783
  _GETVIRTIOSCSILUNREQUEST._serialized_end=3864
  _STATSVIRTIOSCSILUNREQUEST._serialized_start=3866
  _STATSVIRTIOSCSILUNREQUEST._serialized_end=3983
  _STATSVIRTIOSCSILUNRESPONSE._serialized_start=3985
  _STATSVIRTIOSCSILUNRESPONSE._serialized_end=4061
  _FRONTENDVIRTIOSCSISERVICE._serialized_start=4064
  _FRONTENDVIRTIOSCSISERVICE._serialized_end=7409
# @@protoc_insertion_point(module_scope)
