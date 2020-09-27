from django.db.models import Count

from api.modules.aluno.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Aluno


class AlunoListView(IsAutenticatedListApiView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoListSerializer


class AlunoCreateView(IsAutenticatedCreateAPIView):
    serializer_class = AlunoCreateSerializer


class AlunoUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoUpdateSerializer

class AlunoGetView(IsAutenticatedGetApiView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoGetSerializer

class AlunoFilterByUniversidade(IsAutenticatedListApiView):
    serializer_class = AlunoCountByUniversidadeAndAnoSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        queryset = Aluno.objects.filter(id_curso__id_universidade=id).values('enade_ano').annotate(
                total=Count('enade_ano')).order_by('enade_ano')


        return queryset

class AlunoFilterByUniversidadeAndCurso(IsAutenticatedListApiView):
    serializer_class = AlunoCountByUniversidadeAndAnoSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        grupo = self.kwargs['grupo_id']
        queryset = Aluno.objects.filter(id_curso__id_universidade=id, id_curso__codigo_grupo=grupo).values('enade_ano').annotate(
                total=Count('enade_ano')).order_by('enade_ano')


        return queryset

class AlunoFilterByUniversidadeAndAno(IsAutenticatedListApiView):
    serializer_class = AlunoCountByUniversidadeAndAnoSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        ano = self.kwargs['ano']
        queryset = Aluno.objects.filter(id_curso__id_universidade=id, enade_ano=ano).values('enade_ano').annotate(
                total=Count('enade_ano')).order_by('enade_ano')


        return queryset
