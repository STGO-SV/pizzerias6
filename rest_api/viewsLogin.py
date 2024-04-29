from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate



# Create your views here.
@csrf_exempt
@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    username = data.get('username')
    password = data.get('password')

    #Crear un nuevo usuario para token
    #from django.contrib.auth.models import User
    #user = User.objects.create_user(username=username,email='juanito@gmail.com',password=password)
    #user.save()
    
    if username is None or password is None:
        return Response({'error': 'Se requiere un nombre de usuario y una contraseña'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)