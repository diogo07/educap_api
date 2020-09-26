from django.urls import path

from api.modules.aluno.views import AlunoListView, AlunoGetView, AlunoFilterByUniversidade

urlpatterns = [
    path("list", AlunoListView.as_view(), name="aluno_list"),
    path("<int:pk>", AlunoGetView.as_view(), name="aluno_get"),
    path("universidade/<int:id_universidade>", AlunoFilterByUniversidade.as_view(), name="aluno_by_universidade"),
]