from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=50)