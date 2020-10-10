from api.modules.universidade.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Universidade, Curso


class UniversidadeListView(IsAutenticatedListApiView):
    queryset = Universidade.objects.all()
    serializer_class = UniversidadeListSerializer


class UniversidadeCreateView(IsAutenticatedCreateAPIView):
    serializer_class = UniversidadeCreateSerializer


class UniversidadeUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Universidade.objects.all()
    serializer_class = UniversidadeUpdateSerializer


class UniversidadeGetView(IsAutenticatedGetApiView):
    queryset = Universidade.objects.all()
    serializer_class = UniversidadeGetSerializer


class UniversidadeFilterByName(IsAutenticatedListApiView):
    serializer_class = UniversidadeListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        queryset = Universidade.objects.filter(nome__icontains=name)
        if queryset.__len__() > 30:
            return queryset[:30]
        else:
            return queryset

class UniversidadeFilterCursos(IsAutenticatedListApiView):
    serializer_class = UniversidadeFilterCursosSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        queryset = Curso.objects.filter(id_universidade=id).values('id', 'turno', 'codigo_modalidade', 'codigo_grupo')
        return queryset
    