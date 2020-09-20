from api.modules.curso.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Curso


class CursoListView(IsAutenticatedListApiView):
    queryset = Curso.objects.all()
    serializer_class = CursoListSerializer


class CursoCreateView(IsAutenticatedCreateAPIView):
    serializer_class = CursoCreateSerializer


class CursoUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoUpdateSerializer

class CursoGetView(IsAutenticatedGetApiView):
    queryset = Curso.objects.all()
    serializer_class = CursoGetSerializer