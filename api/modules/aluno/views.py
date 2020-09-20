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