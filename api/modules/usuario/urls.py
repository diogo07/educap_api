from django.urls import path

from api.modules.usuario.views import UsuarioListView, UsuarioGetView, UsuarioUsernameValid, UsuarioCreateView, UsuarioUpdateView

urlpatterns = [
    path("create", UsuarioCreateView.as_view(), name="usuario_create"),
    path("update/<int:pk>", UsuarioUpdateView.as_view(), name="usuario_update"),
    path("list", UsuarioListView.as_view(), name="usuario_list"),
    path("<int:pk>", UsuarioGetView.as_view(), name="usuario_get"),
    path("login_available/<str:username>", UsuarioUsernameValid.as_view(), name="usuario_username_valid")
]