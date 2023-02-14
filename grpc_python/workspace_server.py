import grpc
from concurrent import futures
import time
import workspace_pb2_grpc as pb2_grpc
import workspace_pb2 as pb2
from sqlalchemy.orm import sessionmaker
from models import User, Project, Folder, File
from utils import (hash_password,
                    is_password_match,
                    create_access_token,
                    verify_access_token,
                    engine)


class workspaceService(pb2_grpc.workspaceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def UserSignup(self, request, context):
        name = request.name
        password = request.password
        username = request.username
        email = request.email
        hashed_pass = hash_password(password)
        # result = f'I am the server, name of the user is  "{name}"'
        # TODO 
        # check username uniquness  
        result = {}
        user_id = None
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            user = User(name=name, username=username, password=hashed_pass, email=email)
            session.add(user)
            session.commit()
            user_id = user.id
            token = create_access_token({'user_id':user_id,'password':hashed_pass})
            session.close()
        except:
            return pb2.UserDataResponse(**result)
        else:
            result = {'name': name, 'username': username,
                'email': email, 'token': token,
            'userId': user_id}
            return pb2.UserDataResponse(**result)

    def UserLogin(self, request, context):
        password = request.password
        username = request.username
        token = None
        result = {}
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            user = session.query(User).filter_by(username = username).first()
            # session.commit()
            session.close()
        except:
            result = {'message': 'Invalid credentials!'}
            return pb2.UserLoginResponse(**result)
        if is_password_match(password, user.password):
            token = create_access_token({'userId':user.id,'password':user.password})
            result = { 'message':  'Login success!',
                        'token': token,
                        'username': user.username,
                        'userId': user.id}
            return pb2.UserLoginResponse(**result)
        result = {'message': 'Password incorrect!'}
        return pb2.UserLoginResponse(**result)

    def CreateProject(self, request, context):
        name = request.name
        token = request.token
        data = verify_access_token(token)
        result = {}
        owner_id = 0
        project_id = 0
        # import pdb
        # pdb.set_trace()
        if not data:
            result = {'id': 0,
                    'ownerId': 0,
                    'name': "None" }
            #TODO
            return pb2.ProjectMinimalDetail(**result)
        try:
            owner_id = data.get('userId')
            Session = sessionmaker(bind=engine)
            session = Session()
            # user = session.get(User, owner_id)
            project = Project(name=name, user_id=owner_id)
            session.add(project)
            session.commit()
            project_id = project.id
            name = project.name
            # session.commit()
            session.close()
        except:
            result = {'id': 0,
                    'ownerId': 0,
                    'name': "None" }
            #TODO
            return pb2.ProjectMinimalDetail(**{result})
        result = {'id': project_id,
                'ownerId': owner_id,
                'name': name }
        return pb2.ProjectMinimalDetail(**result)

    def CreateFolder(self, request, context):
        name = request.name
        # Either project or folder only
        # If folder is made under a project, or is a root
        # folder, only projectId need to be given
        token = request.token
        data = verify_access_token(token)
        result = {}
        owner_id = 0
        project_id = 0
        folder_id = 0
        if not data:
            result = {'projectId': 0,
                    'ownerId': 0,
                    'name': "None",
                    'id': 0 }
            #TODO fix the response
            return pb2.FolderMinimalDetail(**result)
        try:
            project_id = request.projectId
        except AttributeError:
            pass
        try:
            folder_id = request.folderId
        except AttributeError:
            pass
        new_folder_id = 0
        try:
            owner_id = data.get('userId')
            Session = sessionmaker(bind=engine)
            session = Session()
            # user = session.get(User, owner_id)
            if project_id:
                folder = Folder(name=name, user_id=owner_id, project_id=project_id,
                                            )
            else:
                folder = Folder(name=name, user_id=owner_id, folder_id=folder_id,
                                            )
            session.add(folder)
            session.commit()
            new_folder_id = folder.id
            name = folder.name
            # session.commit()
            session.close()
        except:
            result = {'projectId': 0,
                    'ownerId': 0,
                    'name': "None" }
            #TODO
            return pb2.FolderMinimalDetail(**{result})
        result = {'projectId': project_id,
                'parentFolderId': folder_id,
                'ownerId': owner_id,
                'name': name,
                'id':new_folder_id}
        return pb2.FolderMinimalDetail(**result)

    # def CreateFolderInFolder(self, request, context):
    #     pass

    def CreateFile(self, request, context):
        name = request.name
        # Either project or folder only
        # If folder is made under a project, or is a root
        # folder, only projectId need to be given
        token = request.token
        data = verify_access_token(token)
        result = {}
        owner_id = 0
        folder_id = 0
        if not data:
            result = {'folderId': 0,
                    'ownerId': 0,
                    'name': "None",
                    'id': 0 }
            #TODO fix the response
            return pb2.FileMinimalDetail(**result)
        try:
            project_id = request.projectId
        except AttributeError:
            pass
        try:
            folder_id = request.folderId
        except AttributeError:
            pass
        new_file_id = 0
        try:
            owner_id = data.get('userId')
            Session = sessionmaker(bind=engine)
            session = Session()
            # user = session.get(User, owner_id)
            file = File(name=name, user_id=owner_id, folder_id=folder_id,
                                            )
            session.add(file)
            session.commit()
            new_file_id = file.id
            name = file.name
            # session.commit()
            session.close()
        except:
            result = {'folderId': 0,
                    'ownerId': 0,
                    'name': "None",
                    'id': 0 }
            #TODO
            return pb2.FileMinimalDetail(**{result})
        result = {'folderId': folder_id,
                'ownerId': owner_id,
                'name': name,
                'id':new_file_id}
        return pb2.FileMinimalDetail(**result)

    def UpdateProject(self, request, context):
        pass

    def UpdateFolder(self, request, context):
        pass

    def UpdateFile(self, request, context):
        pass

    def ViewProject(self, request, context):
        pass

    def ViewFolder(self, request, context):
        pass

    def ViewFile(self, request, context):
        pass

    def DeleteProject(self, request, context):
        pass

    def DeleteFolder(self, request, context):
        pass

    def DeleteFile(self, request, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_workspaceServicer_to_server(workspaceService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()