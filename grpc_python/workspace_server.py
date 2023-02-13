import grpc
from concurrent import futures
import time
import workspace_pb2_grpc as pb2_grpc
import workspace_pb2 as pb2


class workspaceService(pb2_grpc.workspaceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def UserSignup(self, request, context):
        name = request.name
        result = f'I am the server, name of the user is  "{name}"'
        # Do db operations
        result = {'name': name, 'received': True}

        return pb2.UserDataResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_workspaceServicer_to_server(workspaceService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()