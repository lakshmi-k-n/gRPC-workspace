import grpc
import workspace_pb2_grpc as pb2_grpc
import workspace_pb2 as pb2

# MAIN CLIENT FILE
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

    def user_signup(self, data):
        """
        Client function that calls method `UserSignup`
        """
        data = pb2.UserData(**data)
        # print(f'{name}')
        # print(data)
        # import pdb
        # pdb.set_trace()
        return self.stub.UserSignup(data)

    def user_login(self, data):
        """
        """
        data = pb2.UserLoginData(**data)
        return self.stub.UserLogin(data)

    def create_project(self, data):
        """
        """
        data = pb2.ProjectData(**data)
        return self.stub.CreateProject(data)

    def create_folder(self, data):
        """
        """
        data = pb2.FolderData(**data)
        return self.stub.CreateFolder(data)

    def create_file(self, data):
        """
        """
        data = pb2.FileData(**data)
        return self.stub.CreateFile(data)

    # def update_project(self, data):
    #     """
    #     """
    #     data = pb2.ProjectId(**data)
    #     return self.stub.UpdateProject(data)

    # def update_folder(self, data):
    #     """
    #     Update folder properties
    #     Move folder to folder
    #     """
    #     data = pb2.FolderId(**data)
    #     return self.stub.UpdateFolder(data)

    # def update_file(self, data):
    #     """
    #     Update file properties
    #     Move file to folder
    #     """
    #     data = pb2.FileId(**data)
    #     return self.stub.UpdateFile(data)

    # def view_project(self, data):
    #     """
    #     Lists contents of a project
    #     """
    #     data = pb2.ProjectId(**data)
    #     return self.stub.ViewProject(data)

    # def view_folder(self, data):
    #     """
    #     Lists contents of a folder
    #     """
    #     data = pb2.FolderId(**data)
    #     return self.stub.ViewFolder(data)

    # def view_file(self, data):
    #     """
    #     view contents of a file
    #     """
    #     data = pb2.FileId(**data)
    #     return self.stub.ViewFile(data)

    # def delete_project(self, data):
    #     """
    #     Delete a project
    #     """
    #     data = pb2.ProjectId(**data)
    #     return self.stub.DeleteProject(data)

    # def delete_folder(self, data):
    #     """
    #     Delete a folder
    #     """
    #     data = pb2.FolderId(**data)
    #     return self.stub.DeleteFolder(data)

    # def delete_file(self, data):
    #     """
    #     Delete a file
    #     """
    #     data = pb2.FileId(**data)
    #     return self.stub.DeleteFile(data)

if __name__ == '__main__':
    client = WorkspaceClient()
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjksInBhc3N3b3JkIjoiJDJiJDEyJDMuV3hNMjdibXk5RHh6Q2VkQzlIS2VoSUdjSzRpVjRqakRtaW5SRHRsZ3lxUmNTbTcucjRtIn0.6DQc_DapjD7FkMKQHyxCf3f90zoJmUEwhx0M0NpTgaE"
    # data = {'name':'lexy', 'password': 'pass', 'email':'email2', 'username': 'lewxy'}
    # result = client.get_signup(data)
    # data = {'username':'lexy', 'password': 'pass'}
    # result = client.user_login(data)
    # data = {'name':'project 1', 'token': token}
    # result = client.create_project(data)
    # data = {'name':'folder 1', 'projectId': 1, 'token': token}
    # result = client.create_folder(data)
    data = {'name':'file 1', 'folderId': 1, 'token': token}
    result = client.create_file(data)
    print(f'{result}')