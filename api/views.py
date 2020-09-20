from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from educap_api.models import Usuario

#
# # Create your views here.
# def login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#
#     user = authenticate(username=username, password=password)
#
#     if user:
#         return HttpResponse('Logado')
#     else:
#         return HttpResponse('Erro login')
#

def jwt_response_payload_handler(token, user=None, request=None):
    context = {'token': token,
               'user': {
                   'username': user.username,
                   'id': user.id,
                   'firt_name': user.first_name,
                   'last_name': user.last_name
               }}
    return context
