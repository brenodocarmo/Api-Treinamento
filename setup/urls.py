from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter


from app.views import AlunoViewSet, TreinamentoViewSet, MatriculaViewSet, ListaMatriculaAluno, ListaCursoAluno


router = DefaultRouter()

router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('treinamentos', TreinamentoViewSet, basename='Treinamentos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')
# router.register('listar', ListaMatriculaAluno, basename='Listar')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/',ListaMatriculaAluno.as_view()),
    path('treinamento/<int:pk>/matriculas/',ListaCursoAluno.as_view())

]
