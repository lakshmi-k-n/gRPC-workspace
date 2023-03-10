# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import workspace_pb2 as workspace__pb2


class workspaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UserSignup = channel.unary_unary(
                '/unary.workspace/UserSignup',
                request_serializer=workspace__pb2.UserData.SerializeToString,
                response_deserializer=workspace__pb2.UserDataResponse.FromString,
                )
        self.UserLogin = channel.unary_unary(
                '/unary.workspace/UserLogin',
                request_serializer=workspace__pb2.UserLoginData.SerializeToString,
                response_deserializer=workspace__pb2.UserLoginResponse.FromString,
                )
        self.CreateProject = channel.unary_unary(
                '/unary.workspace/CreateProject',
                request_serializer=workspace__pb2.ProjectData.SerializeToString,
                response_deserializer=workspace__pb2.ProjectMinimalDetail.FromString,
                )
        self.CreateFolder = channel.unary_unary(
                '/unary.workspace/CreateFolder',
                request_serializer=workspace__pb2.FolderData.SerializeToString,
                response_deserializer=workspace__pb2.FolderMinimalDetail.FromString,
                )
        self.CreateFile = channel.unary_unary(
                '/unary.workspace/CreateFile',
                request_serializer=workspace__pb2.FileData.SerializeToString,
                response_deserializer=workspace__pb2.FileMinimalDetail.FromString,
                )
        self.UpdateFile = channel.unary_unary(
                '/unary.workspace/UpdateFile',
                request_serializer=workspace__pb2.FileData.SerializeToString,
                response_deserializer=workspace__pb2.FileMinimalDetail.FromString,
                )
        self.ViewFile = channel.unary_unary(
                '/unary.workspace/ViewFile',
                request_serializer=workspace__pb2.FileData.SerializeToString,
                response_deserializer=workspace__pb2.FileMinimalDetail.FromString,
                )
        self.ViewProject = channel.unary_unary(
                '/unary.workspace/ViewProject',
                request_serializer=workspace__pb2.ProjectData.SerializeToString,
                response_deserializer=workspace__pb2.ProjectContent.FromString,
                )


class workspaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UserSignup(self, request, context):
        """Workspace rpc declaration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFolder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViewFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViewProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_workspaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UserSignup': grpc.unary_unary_rpc_method_handler(
                    servicer.UserSignup,
                    request_deserializer=workspace__pb2.UserData.FromString,
                    response_serializer=workspace__pb2.UserDataResponse.SerializeToString,
            ),
            'UserLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.UserLogin,
                    request_deserializer=workspace__pb2.UserLoginData.FromString,
                    response_serializer=workspace__pb2.UserLoginResponse.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=workspace__pb2.ProjectData.FromString,
                    response_serializer=workspace__pb2.ProjectMinimalDetail.SerializeToString,
            ),
            'CreateFolder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFolder,
                    request_deserializer=workspace__pb2.FolderData.FromString,
                    response_serializer=workspace__pb2.FolderMinimalDetail.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=workspace__pb2.FileData.FromString,
                    response_serializer=workspace__pb2.FileMinimalDetail.SerializeToString,
            ),
            'UpdateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFile,
                    request_deserializer=workspace__pb2.FileData.FromString,
                    response_serializer=workspace__pb2.FileMinimalDetail.SerializeToString,
            ),
            'ViewFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ViewFile,
                    request_deserializer=workspace__pb2.FileData.FromString,
                    response_serializer=workspace__pb2.FileMinimalDetail.SerializeToString,
            ),
            'ViewProject': grpc.unary_unary_rpc_method_handler(
                    servicer.ViewProject,
                    request_deserializer=workspace__pb2.ProjectData.FromString,
                    response_serializer=workspace__pb2.ProjectContent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'unary.workspace', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class workspace(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UserSignup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/UserSignup',
            workspace__pb2.UserData.SerializeToString,
            workspace__pb2.UserDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UserLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/UserLogin',
            workspace__pb2.UserLoginData.SerializeToString,
            workspace__pb2.UserLoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/CreateProject',
            workspace__pb2.ProjectData.SerializeToString,
            workspace__pb2.ProjectMinimalDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFolder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/CreateFolder',
            workspace__pb2.FolderData.SerializeToString,
            workspace__pb2.FolderMinimalDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/CreateFile',
            workspace__pb2.FileData.SerializeToString,
            workspace__pb2.FileMinimalDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/UpdateFile',
            workspace__pb2.FileData.SerializeToString,
            workspace__pb2.FileMinimalDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViewFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/ViewFile',
            workspace__pb2.FileData.SerializeToString,
            workspace__pb2.FileMinimalDetail.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViewProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.workspace/ViewProject',
            workspace__pb2.ProjectData.SerializeToString,
            workspace__pb2.ProjectContent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
