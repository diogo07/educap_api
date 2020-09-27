from django.urls import path

from api.modules.aluno.views import *

urlpatterns = [
    path("list", AlunoListView.as_view(), name="aluno_list"),
    path("<int:pk>", AlunoGetView.as_view(), name="aluno_get"),
    path("universidade/<int:id_universidade>", AlunoFilterByUniversidade.as_view(), name="aluno_by_universidade"),
    path("universidade/<int:id_universidade>/curso/<int:grupo_id>", AlunoFilterByUniversidadeAndCurso.as_view(), name="aluno_by_universidade_and_curso"),
    path("universidade/<int:id_universidade>/ano/<int:ano>", AlunoFilterByUniversidadeAndAno.as_view(), name="aluno_by_universidade_and_ano"),
]