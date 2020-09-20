from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login', obtain_jwt_token),
    path("municipio/", include('api.modules.municipio.urls'), name="municipio"),
    path("universidade/", include('api.modules.universidade.urls'), name="universidade"),
    path("curso/", include('api.modules.curso.urls'), name="curso"),
    path("aluno/", include('api.modules.aluno.urls'), name="aluno"),
    path("questao/", include('api.modules.questao.urls'), name="questao"),
    path("resposta/", include('api.modules.resposta.urls'), name="resposta"),
    path("usuario/", include('api.modules.usuario.urls'), name="usuario"),

]