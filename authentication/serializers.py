from rest_framework import serializers

from django.contrib.auth.models import User

# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')  # TODO: add role
