from django.urls import path

from api.modules.resposta.views import *

urlpatterns = [
    path("list", RespostaListView.as_view(), name="resposta_list"),
    path("<int:pk>", RespostaGetView.as_view(), name="resposta_get"),
    path("universidade/<int:id_universidade>/ano/<int:ano>", RespostaFilterByUniversidadeEAno.as_view(), name="resposta_by_universidade"),
    path("universidade/<int:id_universidade>/curso/<int:codigo_grupo>/ano/<int:ano>", RespostaFilterByUniversidadeCursoEAno.as_view(), name="resposta_by_universidade_and_curso"),
    path("universidade/<int:id_universidade>/ano/<int:ano>/questao/<str:questao>", RespostaFilterByUniversidadeAnoEQuestao.as_view(), name="resposta_by_universidade_ano_e_questao"),
    path("universidade/<int:id_universidade>/curso/<int:codigo_grupo>/ano/<int:ano>/questao/<str:questao>", RespostaFilterByUniversidadeCursoAnoEQuestao.as_view(), name="resposta_by_universidade_curso_ano_e_questao"),

]
