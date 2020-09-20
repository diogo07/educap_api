from api.modules.questao.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Questao


class QuestaoListView(IsAutenticatedListApiView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoListSerializer


class QuestaoCreateView(IsAutenticatedCreateAPIView):
    serializer_class = QuestaoCreateSerializer


class QuestaoUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoUpdateSerializer

class QuestaoGetView(IsAutenticatedGetApiView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoGetSerializer