from django.urls import path

from api.modules.resposta.views import RespostaListView, RespostaGetView, RespostaFilterByUniversidadeEAno

urlpatterns = [
    path("list", RespostaListView.as_view(), name="resposta_list"),
    path("<int:pk>", RespostaGetView.as_view(), name="resposta_get"),
    path("universidade/<int:id_universidade>/ano/<int:ano>", RespostaFilterByUniversidadeEAno.as_view(), name="resposta_by_universidade"),

]