# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/gizmo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/gizmo.proto\x12\x17\x61\x63me.component.gizmo.v1\x1a\x1cgoogle/api/annotations.proto\"6\n\x0c\x44oOneRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x61rg1\x18\x02 \x01(\tR\x04\x61rg1\"#\n\rDoOneResponse\x12\x12\n\x04ret1\x18\x01 \x01(\x08R\x04ret1\"B\n\x18\x44oOneServerStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x61rg1\x18\x02 \x01(\tR\x04\x61rg1\"/\n\x19\x44oOneServerStreamResponse\x12\x12\n\x04ret1\x18\x01 \x01(\x08R\x04ret1\"B\n\x18\x44oOneClientStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x61rg1\x18\x02 \x01(\tR\x04\x61rg1\"/\n\x19\x44oOneClientStreamResponse\x12\x12\n\x04ret1\x18\x01 \x01(\x08R\x04ret1\"@\n\x16\x44oOneBiDiStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x61rg1\x18\x02 \x01(\tR\x04\x61rg1\"-\n\x17\x44oOneBiDiStreamResponse\x12\x12\n\x04ret1\x18\x01 \x01(\x08R\x04ret1\"6\n\x0c\x44oTwoRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x61rg1\x18\x02 \x01(\x08R\x04\x61rg1\"#\n\rDoTwoResponse\x12\x12\n\x04ret1\x18\x01 \x01(\tR\x04ret12\x9e\x05\n\x0cGizmoService\x12\x8a\x01\n\x05\x44oOne\x12%.acme.component.gizmo.v1.DoOneRequest\x1a&.acme.component.gizmo.v1.DoOneResponse\"2\x82\xd3\xe4\x93\x02,\"*/acme/api/v1/component/gizmo/{name}/do_one\x12|\n\x11\x44oOneClientStream\x12\x31.acme.component.gizmo.v1.DoOneClientStreamRequest\x1a\x32.acme.component.gizmo.v1.DoOneClientStreamResponse(\x01\x12|\n\x11\x44oOneServerStream\x12\x31.acme.component.gizmo.v1.DoOneServerStreamRequest\x1a\x32.acme.component.gizmo.v1.DoOneServerStreamResponse0\x01\x12x\n\x0f\x44oOneBiDiStream\x12/.acme.component.gizmo.v1.DoOneBiDiStreamRequest\x1a\x30.acme.component.gizmo.v1.DoOneBiDiStreamResponse(\x01\x30\x01\x12\x8a\x01\n\x05\x44oTwo\x12%.acme.component.gizmo.v1.DoTwoRequest\x1a&.acme.component.gizmo.v1.DoTwoResponse\"2\x82\xd3\xe4\x93\x02,\"*/acme/api/v1/component/gizmo/{name}/do_twoB*Z(go.acme.com/proto/api/component/gizmo/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.gizmo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(go.acme.com/proto/api/component/gizmo/v1'
  _GIZMOSERVICE.methods_by_name['DoOne']._options = None
  _GIZMOSERVICE.methods_by_name['DoOne']._serialized_options = b'\202\323\344\223\002,\"*/acme/api/v1/component/gizmo/{name}/do_one'
  _GIZMOSERVICE.methods_by_name['DoTwo']._options = None
  _GIZMOSERVICE.methods_by_name['DoTwo']._serialized_options = b'\202\323\344\223\002,\"*/acme/api/v1/component/gizmo/{name}/do_two'
  _DOONEREQUEST._serialized_start=76
  _DOONEREQUEST._serialized_end=130
  _DOONERESPONSE._serialized_start=132
  _DOONERESPONSE._serialized_end=167
  _DOONESERVERSTREAMREQUEST._serialized_start=169
  _DOONESERVERSTREAMREQUEST._serialized_end=235
  _DOONESERVERSTREAMRESPONSE._serialized_start=237
  _DOONESERVERSTREAMRESPONSE._serialized_end=284
  _DOONECLIENTSTREAMREQUEST._serialized_start=286
  _DOONECLIENTSTREAMREQUEST._serialized_end=352
  _DOONECLIENTSTREAMRESPONSE._serialized_start=354
  _DOONECLIENTSTREAMRESPONSE._serialized_end=401
  _DOONEBIDISTREAMREQUEST._serialized_start=403
  _DOONEBIDISTREAMREQUEST._serialized_end=467
  _DOONEBIDISTREAMRESPONSE._serialized_start=469
  _DOONEBIDISTREAMRESPONSE._serialized_end=514
  _DOTWOREQUEST._serialized_start=516
  _DOTWOREQUEST._serialized_end=570
  _DOTWORESPONSE._serialized_start=572
  _DOTWORESPONSE._serialized_end=607
  _GIZMOSERVICE._serialized_start=610
  _GIZMOSERVICE._serialized_end=1280
# @@protoc_insertion_point(module_scope)
