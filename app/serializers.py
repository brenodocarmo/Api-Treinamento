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

    def validate_cpf(self, cpf): 
        if len(cpf) != 11: 
            raise serializers.ValidationError("O cpf deve conter 11 dígitos") 
        return cpf
    
    def validate_rg(self, rg): 
        if len(rg) != 9: 
            raise serializers.ValidationError("O rg deve conter 9 dígitos") 
        return rg
        


class TreinamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treinamento
        fields = '__all__'

    def validate_codigo_curso(self, codigo_curso):
        if len(codigo_curso) != 5:
            raise serializers.ValidationError("O código do curso deve conter 5 dígitos") 
        return codigo_curso


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