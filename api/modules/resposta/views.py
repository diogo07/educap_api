from api.modules.resposta.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Resposta


class RespostaListView(IsAutenticatedListApiView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaListSerializer


class RespostaCreateView(IsAutenticatedCreateAPIView):
    serializer_class = RespostaCreateSerializer


class RespostaUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaUpdateSerializer

class RespostaGetView(IsAutenticatedGetApiView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaGetSerializer