from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User


User = get_user_model()
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'pk', 'email')
