# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/common/action/action.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.node.common.action import (
    action_sequence_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_action__sequence__pb2,
)
from syft.proto.core.node.common.action import (
    garbage_collect_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_garbage__collect__object__pb2,
)
from syft.proto.core.node.common.action import (
    get_enum_attribute_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__enum__attribute__pb2,
)
from syft.proto.core.node.common.action import (
    get_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__object__pb2,
)
from syft.proto.core.node.common.action import (
    get_set_property_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__property__pb2,
)
from syft.proto.core.node.common.action import (
    get_set_static_attribute_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__static__attribute__pb2,
)
from syft.proto.core.node.common.action import (
    run_class_method_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_run__class__method__pb2,
)
from syft.proto.core.node.common.action import (
    run_function_or_constructor_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_run__function__or__constructor__pb2,
)
from syft.proto.core.node.common.action import (
    save_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_save__object__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*proto/core/node/common/action/action.proto\x12\x1csyft.core.node.common.action\x1a.proto/core/node/common/action/get_object.proto\x1a?proto/core/node/common/action/run_function_or_constructor.proto\x1a\x34proto/core/node/common/action/run_class_method.proto\x1a:proto/core/node/common/action/garbage_collect_object.proto\x1a\x36proto/core/node/common/action/get_enum_attribute.proto\x1a\x34proto/core/node/common/action/get_set_property.proto\x1a<proto/core/node/common/action/get_set_static_attribute.proto\x1a/proto/core/node/common/action/save_object.proto\x1a\x33proto/core/node/common/action/action_sequence.proto"\xc6\x06\n\x06\x41\x63tion\x12\x10\n\x08obj_type\x18\x01 \x01(\t\x12J\n\x11get_object_action\x18\x02 \x01(\x0b\x32-.syft.core.node.common.action.GetObjectActionH\x00\x12j\n"run_function_or_constructor_action\x18\x03 \x01(\x0b\x32<.syft.core.node.common.action.RunFunctionOrConstructorActionH\x00\x12U\n\x17run_class_method_action\x18\x04 \x01(\x0b\x32\x32.syft.core.node.common.action.RunClassMethodActionH\x00\x12\x61\n\x1dgarbage_collect_object_action\x18\x06 \x01(\x0b\x32\x38.syft.core.node.common.action.GarbageCollectObjectActionH\x00\x12U\n\x15\x65num_attribute_action\x18\x07 \x01(\x0b\x32\x34.syft.core.node.common.action.GetEnumAttributeActionH\x00\x12Z\n\x1aget_or_set_property_action\x18\x08 \x01(\x0b\x32\x34.syft.core.node.common.action.GetOrSetPropertyActionH\x00\x12\x64\n\x1fget_set_static_attribute_action\x18\t \x01(\x0b\x32\x39.syft.core.node.common.action.GetSetStaticAttributeActionH\x00\x12L\n\x12save_object_action\x18\n \x01(\x0b\x32..syft.core.node.common.action.SaveObjectActionH\x00\x12G\n\x0f\x61\x63tion_sequence\x18\x0b \x01(\x0b\x32,.syft.core.node.common.action.ActionSequenceH\x00\x42\x08\n\x06\x61\x63tionb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "proto.core.node.common.action.action_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ACTION._serialized_start = 578
    _ACTION._serialized_end = 1416
# @@protoc_insertion_point(module_scope)
