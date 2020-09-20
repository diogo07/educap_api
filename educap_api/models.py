from django.db import models
from django.contrib.auth.models import User

class Usuario(User):

    class Meta:
        db_table = 'usuario'

class Aluno(models.Model):
    id = models.IntegerField(primary_key=True)
    idade = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    ano_conc_ens_medio = models.IntegerField(blank=True, null=True)
    ano_inic_grad = models.IntegerField(blank=True, null=True)
    enade_ano = models.IntegerField(blank=True, null=True)
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'


class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    turno = models.CharField(max_length=20)
    id_universidade = models.ForeignKey('Universidade', models.DO_NOTHING, db_column='id_universidade')
    codigo_modalidade = models.IntegerField()
    codigo_grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'
        unique_together = (('id', 'turno', 'id_universidade', 'codigo_modalidade'),)


class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Questao(models.Model):
    codigo = models.CharField(unique=True, max_length=10, blank=True, null=True)
    pergunta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questao'


class Resposta(models.Model):
    codigo_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='codigo_questao', blank=True, null=True)
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno', blank=True, null=True)
    opcao = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta'


class Universidade(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=15, blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universidade'
