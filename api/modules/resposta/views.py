from django.db.models import Count
from django.http import JsonResponse

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

class RespostaFilterByUniversidadeEAno(IsAutenticatedListApiView):
    serializer_class = RespostaFilterByUniversidadeSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        ano = self.kwargs['ano']
        queryset = Resposta.objects.filter(id_aluno__id_curso__id_universidade=id, id_aluno__enade_ano=ano).values('codigo_questao', 'opcao').annotate(
                total=Count('opcao'))

        return queryset