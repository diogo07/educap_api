from api.modules.usuario.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Usuario
from django.contrib.auth.models import User


class UsuarioListView(IsAutenticatedUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer


class UsuarioCreateView(AllowCreateAPIView):
    serializer_class = UsuarioCreateSerializer



class UsuarioUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioUpdateSerializer


class UsuarioGetView(IsAutenticatedUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioGetSerializer


class UsuarioUsernameValid(AllowListAPIView):
    serializer_class = UsuarioListSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = User.objects.filter(username=username)
        return queryset       
