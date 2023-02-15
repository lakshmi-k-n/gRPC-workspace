import grpc
from concurrent import futures
import time
import workspace_pb2_grpc as pb2_grpc
import workspace_pb2 as pb2
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from models import User, Project, Folder, File
from utils import (hash_password,
                    is_password_match,
                    create_access_token,
                    verify_access_token,
                    engine)
from google.protobuf.struct_pb2 import Struct


class workspaceService(pb2_grpc.workspaceServicer):

    def __init__(self, session):
        self.session = session

    def UserSignup(self, request, context):
        name = request.name
        password = request.password
        username = request.username
        email = request.email
        message = ''
        hashed_pass = hash_password(password)
        # TODO 
        result = {}
        user_id = None
        try:
            user = User(name=name, username=username, password=hashed_pass, email=email)
            self.session.add(user)
            self.session.commit()
            user_id = user.id
            token = create_access_token({'user_id':user_id,'password':hashed_pass})
        except:
            message = "Database error!"
            result.update({'message': message})
            return pb2.UserDataResponse(**result)
        result_data = {'name': user.name, 'username': user.username,
                        'email': user.email, 'token': token,
                        'userId': user_id, 'message': message,
                        'success': True}
        result.update(result_data)
        return pb2.UserDataResponse(**result)

    def UserLogin(self, request, context):
        password = request.password
        username = request.username
        token = None
        result = {}
        try:
            import pdb
            pdb.set_trace()
            user = self.session.query(User).filter_by(username = username).first()
        except:
            result = {'message': 'Database error!'}
            return pb2.UserLoginResponse(**result)
        if not user:
            result.update({'message': 'User does not exist!',
                        'success': False})
            return pb2.UserLoginResponse(**result)
        if is_password_match(password, user.password):
            token = create_access_token({'userId':user.id,'password':user.password})
            result.update({ 'message':  'Login success!',
                        'token': token,
                        'username': user.username,
                        'userId': user.id,
                        'success': True})
        else:
            result = {'message': 'Password mismatch!'}
        return pb2.UserLoginResponse(**result)

    def CreateProject(self, request, context):
        name = request.name
        token = request.token
        data = verify_access_token(token)
        result = {}
        owner_id = 0
        project_id = 0
        if not data:
            result.update({'message': 'User not authenticated!' })
            return pb2.ProjectMinimalDetail(**result)
        try:
            owner_id = data.get('userId')
            project = Project(name=name, user_id=owner_id)
            self.session.add(project)
            self.session.commit()
        except:
            result.update({'message': "Database Error!"})
            #TODO
            return pb2.ProjectMinimalDetail(**{result})
        project_id = project.id
        name = project.name
        result.update({'id': project_id,
                'ownerId': owner_id,
                'name': name ,
                'message': 'Success!',
                'success': True})
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
        new_folder_id = 0
        if not data:
            result.update({'message': 'User not authenticated!' })
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
        if not project_id and not folder_id:
            result.update({'message': 'Project id or folder id not provided!' })
            return pb2.FolderMinimalDetail(**result)
        try:
            owner_id = data.get('userId')
            # user = session.get(User, owner_id)
            if project_id:
                folder = Folder(name=name, user_id=owner_id, project_id=project_id,
                                            )
            else:
                folder = Folder(name=name, user_id=owner_id, folder_id=folder_id,
                                            )
            self.session.add(folder)
            self.session.commit()
        except:
            result.update({'message': 'Database error!' })
            #TODO
            return pb2.FolderMinimalDetail(**{result})
        new_folder_id = folder.id
        name = folder.name
        result.update({'projectId': project_id,
                'parentFolderId': folder_id,
                'ownerId': owner_id,
                'name': name,
                'id':new_folder_id,
                'message': 'Success!'})
        return pb2.FolderMinimalDetail(**result)

    def CreateFile(self, request, context):
        name = request.name
        content = request.content
        folder_id = request.folderId
        token = request.token
        data = verify_access_token(token)
        result = {}
        owner_id = 0
        folder_id = 0
        new_file_id = 0
        if not data:
            result = {'message': 'User not authenticated!'}
            #TODO fix the response
            return pb2.FileMinimalDetail(**result)
        try:
            folder_id = request.folderId
        except AttributeError:
            result = {'message': 'Folder id not provided!'}
            return pb2.FileMinimalDetail(**result)
        try:
            owner_id = data.get('userId')
            file = File(name=name, user_id=owner_id,
                        folder_id=folder_id,
                        content=content)
            self.session.add(file)
            self.session.commit()
        except:
            result.update
            #TODO
            return pb2.FileMinimalDetail(**{result})
        new_file_id = file.id
        name = file.name
        result = {'folderId': folder_id,
                'ownerId': owner_id,
                'name': name,
                'id':new_file_id,
                'content': content,
                'message': 'Success!'}
        return pb2.FileMinimalDetail(**result)

    def UpdateFolder(self, request, context):
        pass

    def UpdateFile(self, request, context):
        file_id = request.id
        folder_id = request.folderId
        name = request.name
        content = request.content
        token = request.token
        data = verify_access_token(token)
        result = {}
        if not data:
            result = {'message': 'User not authenticated!'}
            return pb2.FileMinimalDetail(**result)
        owner_id = data.get('userId')
        if not self.session.get(File, file_id):
            result = {'message': 'File does not exist!'}
            return pb2.FileMinimalDetail(**result)
        file = self.session.query(File).filter_by(user_id=owner_id,id=file_id).first()
        if not file:
            result = {'message': 'User does not own this file!'}
            return pb2.FileMinimalDetail(**result)
        if folder_id:
            if not self.session.get(Folder, folder_id):
                result = {'message': 'Target folder does not exist!'}
                return pb2.FileMinimalDetail(**result)
            file.folder_id = folder_id
        if name:
            file.name = name
        if content:
            file.content = content
        self.session.commit()

        result = {
                'ownerId': owner_id,
                'name': file.name,
                'folderId': file.folder_id,
                'id':file.id,
                'content': file.content,
                'message': 'Success!'}
        return pb2.FileMinimalDetail(**result)

    def ViewProject(self, request, context):
        # ProjectContent
        project_id = request.id
        result = {}
        project = self.session.get(Project, project_id)
        if not project:
            result = {'message': 'Project does not exist!'}
            return pb2.ProjectContent(**result)
        folders =  self.session.query(Folder).filter_by(project_id=project_id)
        folders_list = []
        item_dict = {}
        for folder in folders:
            item_dict.update({'id': folder.id,
                              'name': folder.name,
                              'owner':folder.user.username})
            folders_list.append(item_dict)
        struct = Struct()
        struct.update({'folders_list':folders_list})
        result.update({'id': project_id,
                        'name': project.name,
                        'content': struct,
                        'message': "Success!",
                        'success': True
                        })
        return pb2.ProjectContent(**result)

    def ViewFolder(self, request, context):
        pass

    def ViewFile(self, request, context):
        '''
        '''
        file_id = request.id
        result = {}
        # import pdb
        # pdb.set_trace()
        if not self.session.get(File, file_id):
            result = {'message': 'File does not exist!'}
            return pb2.FileMinimalDetail(**result)
        file = self.session.query(File).filter_by(id=file_id).first()
        if not file:
            result = {'message': 'File does not exist!'}
        result = {
                'ownerId': file.user_id,
                'name': file.name,
                'folderId': file.folder_id,
                'id':file.id,
                'content': file.content,
                'message': 'Success!'}
        return pb2.FileMinimalDetail(**result)
        

def serve():
    with Session(engine) as session, session.begin():
        workspace_service = workspaceService(session)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_workspaceServicer_to_server(workspace_service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()