from api.modules.municipio.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Municipio


class MunicipioListView(IsAutenticatedListApiView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioListSerializer


class MunicipioCreateView(IsAutenticatedCreateAPIView):
    serializer_class = MunicipioCreateSerializer


class MunicipioUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioUpdateSerializer

class MunicipioGetView(IsAutenticatedGetApiView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioGetSerializer