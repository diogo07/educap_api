from django.urls import path

from api.modules.questao.views import QuestaoListView, QuestaoGetView

urlpatterns = [
    path("list", QuestaoListView.as_view(), name="questao_list"),
    path("<int:pk>", QuestaoGetView.as_view(), name="questao_get")
]