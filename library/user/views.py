from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = request.data
        username = data['name']
        email = data['email']
        password = data['password']

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'User with this name exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user: User = User.objects.create_user(username=username, email=email, password=password)

        return Response({'userId': user.pk}, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    def get(self, request):
        user = request.user
        user = UserSerializer(user)
        return Response(
            {'user': user.data},
            status=status.HTTP_200_OK
        )
