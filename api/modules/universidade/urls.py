from django.urls import path

from api.modules.universidade.views import UniversidadeListView, UniversidadeGetView, UniversidadeFilterByName

urlpatterns = [
    path("list", UniversidadeListView.as_view(), name="universidade_list"),
    path("<int:pk>", UniversidadeGetView.as_view(), name="universidade_get"),
    path("<str:name>", UniversidadeFilterByName.as_view(), name="universidade_filter")
]