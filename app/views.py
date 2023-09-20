from rest_framework import viewsets, generics
from app.models import Aluno, Treinamento, Matricula

from app.serializers import AlunoSerializer, TreinamentoSerializer, MatriculaSerializer, ListaMatriculaerializer, ListaCursoAlunoSerializer
class AlunoViewSet(viewsets.ModelViewSet):
    """
    Exibindo alunos
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TreinamentoViewSet(viewsets.ModelViewSet):
    """
    Exibindo treinamentos
    """
    queryset = Treinamento.objects.all()
    serializer_class = TreinamentoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Exibindo as matriculas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaAluno(generics.ListAPIView):
    """
    Exibindo os cursos de um aluno
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])

        return queryset
    serializer_class = ListaMatriculaerializer

class ListaCursoAluno(generics.ListAPIView):
    """
    Exibindo os alunos por curso
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(treinamento_id=self.kwargs['pk'])

        return queryset
    serializer_class = ListaCursoAlunoSerializer


