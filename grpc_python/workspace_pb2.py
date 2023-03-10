# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workspace.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fworkspace.proto\x12\x05unary\x1a\x1cgoogle/protobuf/struct.proto\"K\n\x08UserData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"\x82\x01\n\x10UserDataResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t\x12\x0e\n\x06userId\x18\x05 \x01(\x05\x12\x0f\n\x07message\x18\x06 \x01(\t\x12\x0f\n\x07success\x18\x07 \x01(\x08\" \n\rErrorResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"3\n\rUserLoginData\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"x\n\x11UserLoginResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x0e\n\x06userId\x18\x05 \x01(\x05\x12\x0f\n\x07success\x18\x06 \x01(\x08\"6\n\x0bProjectData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\"c\n\x14ProjectMinimalDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07ownerId\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x0f\n\x07success\x18\x05 \x01(\x08\"v\n\x0eProjectContent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12(\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x0f\n\x07success\x18\x05 \x01(\x08\"T\n\nFolderData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eparentFolderId\x18\x02 \x01(\x05\x12\x11\n\tprojectId\x18\x03 \x01(\x05\x12\r\n\x05token\x18\x04 \x01(\t\"\x8d\x01\n\x13\x46olderMinimalDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eparentFolderId\x18\x02 \x01(\x05\x12\x11\n\tprojectId\x18\x03 \x01(\x05\x12\x0f\n\x07ownerId\x18\x04 \x01(\x05\x12\n\n\x02id\x18\x05 \x01(\x05\x12\x0f\n\x07message\x18\x06 \x01(\t\x12\x0f\n\x07success\x18\x07 \x01(\x08\"V\n\x08\x46ileData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x10\n\x08\x66olderId\x18\x03 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\x05\"\x83\x01\n\x11\x46ileMinimalDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07ownerId\x18\x02 \x01(\x05\x12\x10\n\x08\x66olderId\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x05\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x0f\n\x07success\x18\x06 \x01(\x08\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t2\xf4\x03\n\tworkspace\x12\x38\n\nUserSignup\x12\x0f.unary.UserData\x1a\x17.unary.UserDataResponse\"\x00\x12=\n\tUserLogin\x12\x14.unary.UserLoginData\x1a\x18.unary.UserLoginResponse\"\x00\x12\x42\n\rCreateProject\x12\x12.unary.ProjectData\x1a\x1b.unary.ProjectMinimalDetail\"\x00\x12?\n\x0c\x43reateFolder\x12\x11.unary.FolderData\x1a\x1a.unary.FolderMinimalDetail\"\x00\x12\x39\n\nCreateFile\x12\x0f.unary.FileData\x1a\x18.unary.FileMinimalDetail\"\x00\x12\x39\n\nUpdateFile\x12\x0f.unary.FileData\x1a\x18.unary.FileMinimalDetail\"\x00\x12\x37\n\x08ViewFile\x12\x0f.unary.FileData\x1a\x18.unary.FileMinimalDetail\"\x00\x12:\n\x0bViewProject\x12\x12.unary.ProjectData\x1a\x15.unary.ProjectContent\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workspace_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERDATA._serialized_start=56
  _USERDATA._serialized_end=131
  _USERDATARESPONSE._serialized_start=134
  _USERDATARESPONSE._serialized_end=264
  _ERRORRESPONSE._serialized_start=266
  _ERRORRESPONSE._serialized_end=298
  _USERLOGINDATA._serialized_start=300
  _USERLOGINDATA._serialized_end=351
  _USERLOGINRESPONSE._serialized_start=353
  _USERLOGINRESPONSE._serialized_end=473
  _PROJECTDATA._serialized_start=475
  _PROJECTDATA._serialized_end=529
  _PROJECTMINIMALDETAIL._serialized_start=531
  _PROJECTMINIMALDETAIL._serialized_end=630
  _PROJECTCONTENT._serialized_start=632
  _PROJECTCONTENT._serialized_end=750
  _FOLDERDATA._serialized_start=752
  _FOLDERDATA._serialized_end=836
  _FOLDERMINIMALDETAIL._serialized_start=839
  _FOLDERMINIMALDETAIL._serialized_end=980
  _FILEDATA._serialized_start=982
  _FILEDATA._serialized_end=1068
  _FILEMINIMALDETAIL._serialized_start=1071
  _FILEMINIMALDETAIL._serialized_end=1202
  _WORKSPACE._serialized_start=1205
  _WORKSPACE._serialized_end=1705
# @@protoc_insertion_point(module_scope)
