from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import api_view

role_types = ["read_product", "manage_product", "read_manage_product", "admin"]

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def login(request, role_type):
    if not role_type in role_types:
        return Response(data={"details": "Not found URL."}, status=status.HTTP_404_NOT_FOUND)
    if not 'username' in request.data :
        return Response(data={"username": "This field is required."}, status=status.HTTP_200_OK)
    if not 'password' in request.data:
        return Response(data={"password": "This field is required."}, status=status.HTTP_200_OK)

    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        token = get_tokens_for_user(user)
        user.role = role_types.index(role_type)
        user.save()
        return Response(data=token,status=status.HTTP_200_OK)
    else:
        return Response(data={"detail": "No active account found with the given credentials"},status=status.HTTP_200_OK)