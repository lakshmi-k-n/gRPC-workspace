from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from probuf_client.workspace_client import WorkspaceClient
from google.protobuf.json_format import MessageToDict

from .serializers import UserSerializer


class SignUpAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = {}
        client = WorkspaceClient()
        try:
            result = client.user_signup(data)
        except:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)


class ProjectAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        #TODO Validate data, with a serializer
        if 'token' not in data:
            return Response({'message': 'token missing'}, status=status.HTTP_400_BAD_REQUEST)
        client = WorkspaceClient()
        try:
            result = client.create_project(data)
        except:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        project_id = request.query_params.get('id')
        response = {}
        data = {}
        if project_id:
            client = WorkspaceClient()
            try:
                data['id'] = int(project_id)
                result = client.view_project(data)
            except:
                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            response = MessageToDict(result)
        return Response(response, status=status.HTTP_200_OK)


class FolderAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        response = {}
        #TODO Validate data, with a serializer
        client = WorkspaceClient()
        try:
            result = client.create_folder(data)
        except:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)


class FileAPI(APIView):

    def post(self, request, format=None):
        data=request.data
        if 'token' not in data:
            return Response({'message': 'token missing'}, status=status.HTTP_400_BAD_REQUEST)
        #TODO Validate data, with a serializer
        response = {}
        client = WorkspaceClient()
        try:
            result = client.create_file(data)
        except:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        file_id = request.query_params.get('id')
        response = {}
        data = {}
        if file_id:
            client = WorkspaceClient()
            try:
                data['id'] = int(file_id)
                result = client.view_file(data)
            except:
                return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)
            response = MessageToDict(result)
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        data=request.data
        if 'token' not in data:
            return Response({'message': 'token missing'}, status=status.HTTP_400_BAD_REQUEST)
        #TODO Validate data, with a serializer
        response = {}
        client = WorkspaceClient()
        try:
            result = client.update_file(data)
        except:
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response = MessageToDict(result)
        return Response(response, status=status.HTTP_201_CREATED)
