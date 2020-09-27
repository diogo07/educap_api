from django.urls import path

from api.modules.universidade.views import *

urlpatterns = [
    path("list", UniversidadeListView.as_view(), name="universidade_list"),
    path("<int:pk>", UniversidadeGetView.as_view(), name="universidade_get"),
    path("<int:id_universidade>/cursos", UniversidadeFilterCursos.as_view(), name="universidade_cursos_filter"),
    path("<str:name>", UniversidadeFilterByName.as_view(), name="universidade_filter")
]