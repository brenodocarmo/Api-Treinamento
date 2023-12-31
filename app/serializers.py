from rest_framework import serializers

from validate_docbr import CPF



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
        """
        Função para validar o tamanho do CPF
        """

        v_cpf = CPF()

        if not v_cpf.validate(cpf):
                raise serializers.ValidationError("Você deve digitar um CPF válido")
        return v_cpf



    def validate_rg(self, rg): 
        """
        Função para validar o tamanho do RG
        """
        if not rg.isdigit():
            raise serializers.ValidationError("Você deve digitar apenas numeros")

        if len(rg) != 9: 
            raise serializers.ValidationError("O rg deve conter 9 dígitos") 
        return rg
        



class TreinamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treinamento
        fields = '__all__'

    def validate_codigo_curso(self, codigo_curso):
        """
        Função para validar o codigo do curso, dessa forma, 
        o sistema anula a duplicação do mesmo codigo do curso.
        """
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