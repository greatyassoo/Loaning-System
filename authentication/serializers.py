from rest_framework import serializers

from .models import CustomUser
from .auth_enums import UserRole

# Create your views here.


class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[(tag, tag.value) for tag in UserRole])

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'role']
