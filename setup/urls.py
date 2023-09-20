from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.views import AlunoViewSet, TreinamentoViewSet, MatriculaViewSet, ListaMatriculaAluno, ListaCursoAluno


schema_view = get_schema_view(
   openapi.Info(
      title="API Treinamento",
      default_version='v1',
      description="Realiza cadastro de Alunos e Treinamentos, assim como criar os vinculos entre eles",
      terms_of_service="#",
      contact=openapi.Contact(email="brenocarmosousa@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()

router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('treinamentos', TreinamentoViewSet, basename='Treinamentos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')
# router.register('listar', ListaMatriculaAluno, basename='Listar')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/',ListaMatriculaAluno.as_view()),
    path('treinamento/<int:pk>/matriculas/',ListaCursoAluno.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'),

]
