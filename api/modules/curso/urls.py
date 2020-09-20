from django.urls import path

from api.modules.curso.views import CursoListView, CursoGetView

urlpatterns = [
    path("list", CursoListView.as_view(), name="Curso_list"),
    path("<int:pk>", CursoGetView.as_view(), name="Curso_get")
]