from rest_framework import serializers

from app.models import Aluno, Treinamento, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    """
    Serializers: Seria uma forma que realizar um filtro
    dos campos que desejamos exibir atraves da API
    """
    class Meta:
        model = Aluno # Modelo que será utilizado
        fields = [
            'id',
            'nome',
            'rg',
            'cpf',
            'data_nascimento'
        ] # Campos que será utilizados na serialização


class TreinamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treinamento
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculaerializer(serializers.ModelSerializer):

    treinamento = serializers.ReadOnlyField(source='treinamento.nome_treinamento')
    class Meta:
        model = Matricula
        fields = [
            'treinamento'
            ]

class ListaCursoAlunoSerializer(serializers.ModelSerializer):

    aluno = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno']