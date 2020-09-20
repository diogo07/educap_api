# Generated by Django 3.1.1 on 2020-09-13 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
                ('ano_conc_ens_medio', models.IntegerField(blank=True, null=True)),
                ('ano_inic_grad', models.IntegerField(blank=True, null=True)),
                ('enade_ano', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('turno', models.CharField(max_length=20)),
                ('codigo_modalidade', models.IntegerField()),
                ('codigo_grupo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('pergunta', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'questao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'resposta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Universidade',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('departamento', models.CharField(blank=True, max_length=20, null=True)),
                ('categoria', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'universidade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
