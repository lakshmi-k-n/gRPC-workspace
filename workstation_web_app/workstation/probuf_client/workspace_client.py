import grpc
from . import workspace_pb2_grpc as pb2_grpc
from . import workspace_pb2 as pb2
from google.protobuf.json_format import MessageToDict

# MAIN CLIENT FILE
class WorkspaceClient(object):
    """
    gRPC client
    """
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.workspaceStub(self.channel)

    def user_signup(self, data):
        """
        Client method that calls method `UserSignup`
        """
        data = pb2.UserData(**data)
        return self.stub.UserSignup(data)

    def user_login(self, data):
        """
        Client method that calls method `UserLogin`
        """
        data = pb2.UserLoginData(**data)
        return self.stub.UserLogin(data)

    def create_project(self, data):
        """
        Client method that calls method `CreateProject`
        """
        data = pb2.ProjectData(**data)
        return self.stub.CreateProject(data)

    def create_folder(self, data):
        """
        Client method that calls method `CreateFolder`
        """
        data = pb2.FolderData(**data)
        return self.stub.CreateFolder(data)

    def create_file(self, data):
        """
        Client method that calls method `CreateFile`
        """
        data = pb2.FileData(**data)
        return self.stub.CreateFile(data)

    def view_project(self, data):
        """
        Client method that calls method `ViewProject`
        Lists folders inside a project
        """
        data = pb2.ProjectData(**data)
        return self.stub.ViewProject(data)

    def view_file(self, data):
        """
        Client method that calls method `ViewFile`
        """
        data = pb2.FileData(**data)
        return self.stub.ViewFile(data)

    def update_file(self, data):
        """
        Client method that calls method `UpdateFile`
        Update file properties
        Move file to folder
        """
        data = pb2.FileData(**data)
        return self.stub.UpdateFile(data)


if __name__ == '__main__':
    client = WorkspaceClient()
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjksInBhc3N3b3JkIjoiJDJiJDEyJDMuV3hNMjdibXk5RHh6Q2VkQzlIS2VoSUdjSzRpVjRqakRtaW5SRHRsZ3lxUmNTbTcucjRtIn0.6DQc_DapjD7FkMKQHyxCf3f90zoJmUEwhx0M0NpTgaE"
    # data = {"name":"aleena", "paswword": "aleena", "email":"emails8", "username": "aleena"}
    # 
    # result = client.user_signup(data)
    # data = {"username":"lexy", "password": "pass"}
    # result = client.user_login(data)
    # data = {"name":"project armageddon", "token": token}
    # result = client.create_project(data)
    # data = {"name":"folder 5", "projectId": 4, "token": token}
    # result = client.create_folder(data)
    # data = {"name":"file test 2", "folderId": 3,"content":"This is file content", "token": token}
    # result = client.create_file(data)
    # data = {'id':6, 'name':'file test 2', 'content':"This is file content modified", 'token': token}
    # result = client.update_file(data)
    # data = {"id":6, "name":"file test 3", "folderId":2, "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjksInBhc3N3b3JkIjoiJDJiJDEyJDMuV3hNMjdibXk5RHh6Q2VkQzlIS2VoSUdjSzRpVjRqakRtaW5SRHRsZ3lxUmNTbTcucjRtIn0.6DQc_DapjD7FkMKQHyxCf3f90zoJmUEwhx0M0NpTgaE"}
    # result = client.update_file(data)
    # data = {'id':6}
    # result = client.view_file(data)
    data = {'id':1,'token': token}
    result = client.view_project(data)
    result = MessageToDict(result)
    print(result)