from django.db.models import Count
from django.db import connection


from api.modules.resposta.serializers import *
from api.modules.basicApiView import *
from educap_api.models import Resposta


class RespostaListView(IsAutenticatedListApiView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaListSerializer


class RespostaCreateView(IsAutenticatedCreateAPIView):
    serializer_class = RespostaCreateSerializer


class RespostaUpdateView(IsAutenticatedUpdateAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaUpdateSerializer

class RespostaGetView(IsAutenticatedGetApiView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaGetSerializer

class RespostaFilterByUniversidadeEAno(IsAutenticatedListApiView):
    serializer_class = RespostaFilterByUniversidadeSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        ano = self.kwargs['ano']
        queryset = Resposta.objects.filter(id_aluno__id_curso__id_universidade=id, id_aluno__enade_ano=ano).values('codigo_questao', 'opcao').annotate(
                total=Count('opcao'))

        return queryset

class RespostaFilterByUniversidadeCursoEAno(IsAutenticatedListApiView):
    serializer_class = RespostaFilterByUniversidadeSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        ano = self.kwargs['ano']
        codigo_grupo = self.kwargs['codigo_grupo']
        queryset = Resposta.objects.filter(id_aluno__id_curso__id_universidade=id, id_aluno__id_curso__codigo_grupo=codigo_grupo, id_aluno__enade_ano=ano).values('codigo_questao', 'opcao').annotate(
                total=Count('opcao'))

        return queryset

class RespostaFilterByUniversidadeAnoEQuestao(IsAutenticatedListApiView):
    serializer_class = RespostaFilterByUniversidadeSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        ano = self.kwargs['ano']
        codigo_questao = self.kwargs['questao']
        cursor = connection.cursor()
        cursor.execute("select r.codigo_questao as codigo_questao, r.opcao as opcao, count(r.opcao) as total from resposta as r"+
                                        " inner join aluno as al on al.id = r.id_aluno"+
                                        " inner join curso as cr on cr.id = al.id_curso"+
                                        " inner join universidade as u on u.id = cr.id_universidade"+
                                        " inner join questao as q on q.codigo = r.codigo_questao"+
                                        " where r.codigo_questao = '"+codigo_questao+"' and u.id = "+str(id)+" and al.enade_ano = "+str(ano)+""+
                                        " group by (r.opcao, r.codigo_questao)")
        queryset = []
        for q in cursor.fetchall():
            queryset.append({
                'codigo_questao': q[0],
                'opcao': q[1],
                'total': q[2]
            })
        return queryset

class RespostaFilterByUniversidadeCursoAnoEQuestao(IsAutenticatedListApiView):
    serializer_class = RespostaFilterByUniversidadeSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        ano = self.kwargs['ano']
        codigo_grupo = self.kwargs['codigo_grupo']
        codigo_questao = self.kwargs['questao']
        cursor = connection.cursor()
        cursor.execute(
            "select r.codigo_questao as codigo_questao, r.opcao as opcao, count(r.opcao) as total from resposta as r" +
            " inner join aluno as al on al.id = r.id_aluno" +
            " inner join curso as cr on cr.id = al.id_curso" +
            " inner join universidade as u on u.id = cr.id_universidade" +
            " inner join questao as q on q.codigo = r.codigo_questao" +
            " where r.codigo_questao = '" + codigo_questao + "' and u.id = " + str(id) + " and al.enade_ano = " + str(
                ano) + " and cr.codigo_grupo = " + str(codigo_grupo) +
            " group by (r.opcao, r.codigo_questao)")
        queryset = []
        for q in cursor.fetchall():
            queryset.append({
                'codigo_questao': q[0],
                'opcao': q[1],
                'total': q[2]
            })
        return queryset

class RespostaFilterByUniversidadeEPercepcaoProva(IsAutenticatedListApiView):
    serializer_class = RespostaFilterByUniversidadeEPercepcaoProvaSerializer

    def get_queryset(self):
        id = self.kwargs['id_universidade']
        cursor = connection.cursor()
        cursor.execute(
            "select al.enade_ano, r.opcao as opcao, count(r.opcao) as total from resposta as r" +
            " inner join aluno as al on al.id = r.id_aluno" +
            " inner join curso as cr on cr.id = al.id_curso" +
            " inner join universidade as u on u.id = cr.id_universidade" +
            " inner join questao as q on q.codigo = r.codigo_questao" +
            " where r.codigo_questao in ('QE_I28', 'QE_I29', 'QE_I30', 'QE_I31', 'QE_I32', 'QE_I33', 'QE_I34', 'QE_I35', 'QE_I36', 'QE_I37', 'QE_I38', 'QE_I39', 'QE_I40', 'QE_I41', 'QE_I42', 'QE_I43', 'QE_I44', 'QE_I45', 'QE_I46', 'QE_I47', 'QE_I48', 'QE_I49', 'QE_I50', 'QE_I51', 'QE_I52', 'QE_I53', 'QE_I54', 'QE_I55', 'QE_I56', 'QE_I57', 'QE_I58', 'QE_I59', 'QE_I60', 'QE_I61', 'QE_I62', 'QE_I63', 'QE_I64', 'QE_I65', 'QE_I66', 'QE_I67', 'QE_I68') and u.id = " + str(id) +
            " group by (al.enade_ano, r.opcao) order by al.enade_ano, r.opcao")
        queryset = []

        for q in cursor.fetchall():
            queryset.append({
                'ano': q[0],
                'opcao': q[1],
                'total': q[2]
            })
        return queryset