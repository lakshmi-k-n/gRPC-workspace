from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from probuf_client.workspace_client import WorkspaceClient
from google.protobuf.json_format import MessageToDict


class SignUpAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        client = WorkspaceClient()
        #TODO Validate data, with a serializer
        try:
            result = client.user_signup(data)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        client = WorkspaceClient()
        #TODO Validate data, with a serializer
        try:
            result = client.user_login(data)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)


class ProjectAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        client = WorkspaceClient()
        #TODO Validate data, with a serializer
        try:
            result = client.create_project(data)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        project_id = request.query_params.get('id')
        response = {}
        data = {}
        if project_id:
            client = WorkspaceClient()
            #TODO Validate data, with a serializer
            try:
                data['id'] = int(project_id)
                result = client.view_project(data)
            except:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            response = MessageToDict(result)
        return Response(response, status=status.HTTP_200_OK)


class FolderAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        client = WorkspaceClient()
        #TODO Validate data, with a serializer
        try:
            result = client.create_folder(data)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)


class FileAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        client = WorkspaceClient()
        #TODO Validate data, with a serializer
        try:
            result = client.create_file(data)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        file_id = request.query_params.get('id')
        response = {}
        data = {}
        if file_id:
            client = WorkspaceClient()
            #TODO Validate data, with a serializer
            try:
                data['id'] = int(file_id)
                result = client.view_file(data)
            except:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            response = MessageToDict(result)
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        data=request.data
        response = {}
        client = WorkspaceClient()
        #TODO Validate data, with a serializer
        try:
            result = client.update_file(data)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)
