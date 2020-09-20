from django.urls import path

from api.modules.resposta.views import RespostaListView, RespostaGetView

urlpatterns = [
    path("list", RespostaListView.as_view(), name="resposta_list"),
    path("<int:pk>", RespostaGetView.as_view(), name="resposta_get")
]