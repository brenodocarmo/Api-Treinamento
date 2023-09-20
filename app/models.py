from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Treinamento(models.Model):

    CATEGORIA = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    codigo_curso = models.CharField(max_length=10)
    nome_treinamento = models.CharField(max_length=30, default=False)
    descricao = models.CharField(max_length=500)
    categoria = models.CharField(
        max_length=1, 
        choices=CATEGORIA,
        blank=False, # Obriga que o curso tenha uma categoria
        null=False,
        default='B' # Quando o curso não tenha nenhuma representaçao, ele ficará com B - Básico
        )
    

    def __str__(self):
        return self.nome_treinamento
    

class Matricula(models.Model):

    aluno = models.ForeignKey(
            Aluno, 
            on_delete=models.CASCADE
            ) # Quando o aluno for excluido a sua matricula será deletado 
    treinamento = models.ForeignKey(
        Treinamento, 
        on_delete=models.CASCADE
        ) 