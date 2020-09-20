from api.modules.usuario.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Usuario
from django.contrib.auth.models import User


class UsuarioListView(AllowListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer


class UsuarioCreateView(AllowCreateAPIView):
    serializer_class = UsuarioCreateSerializer



class UsuarioUpdateView(AllowUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioUpdateSerializer


class UsuarioGetView(AllowGetAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioGetSerializer


class UsuarioUsernameValid(AllowListAPIView):
    serializer_class = UsuarioListSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = User.objects.filter(username__icontains=username)
        return queryset
        # if queryset.__len__() > 0:
        #     # return {'login_available': 'false'}
        #     return 0
        # else:
        #     # return {'login_available': 'true'}
        #     return 1