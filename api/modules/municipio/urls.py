from django.urls import path

from api.modules.municipio.views import MunicipioListView, MunicipioGetView

urlpatterns = [
    path("list", MunicipioListView.as_view(), name="municipio_list"),
    path("<int:pk>", MunicipioGetView.as_view(), name="municipio_get")
]