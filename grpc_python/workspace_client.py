import grpc
import workspace_pb2_grpc as pb2_grpc
import workspace_pb2 as pb2


class WorkspaceClient(object):
    """
    Client for gRPC functionality
    """
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.workspaceStub(self.channel)

    def get_signup(self, name):
        """
        Client function that calls method `UserSignup`
        """
        name = pb2.UserData(name=name)
        print(f'{name}')
        # import pdb
        # pdb.set_trace()
        return self.stub.UserSignup(name)


if __name__ == '__main__':
    client = WorkspaceClient()
    result = client.get_signup(name="Lakshmi")
    print(f'{result}')