from django.contrib import admin
from app.models import Aluno, Treinamento, Matricula
# Register your models here.

class AlunosAdmin(admin.ModelAdmin):

    list_display = (
        # Campos que serão exibidos no Admin
        'id', 
        'nome',
        'data_nascimento'
    )

    list_display_links = (
        # Campos a serem usados como links clicáveis
        'id',
        'nome'
    )

    search_fields = (
        # Campos a serem usados para pesquisa
        'id',
        'nome',
        'cpf'
    )

    list_per_page = 20 # Número de registros exibidos por página

admin.site.register(Aluno, AlunosAdmin)


class TreinamentoAdmin(admin.ModelAdmin):
   
    list_display = (
        'id',
        'codigo_curso',
        'nome_treinamento',
        'descricao'
    )

    list_display_links = (
        'id',
        'codigo_curso',
        'nome_treinamento'
    )

    search_fields = (
        'codigo_curso',
        'nome_treinamento'
    )

    list_per_page = 20

admin.site.register(Treinamento, TreinamentoAdmin)


class MatriculaAdmm(admin.ModelAdmin):
    
    list_display = (
        'id',
        'aluno',
        'treinamento'
    )

    list_display_links = (
        'id',
        'aluno',
        'treinamento'
    )

    search_fields = (
        'aluno',
        'treinamento'
    )

admin.site.register(Matricula, MatriculaAdmm)



