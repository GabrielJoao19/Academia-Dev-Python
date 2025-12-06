from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('auth/', include('rest_framework.urls')),
    path('', include('home.urls')),
    path('cursos/', include('cursos.urls')),
    path('alunos/', include('alunos.urls')),
    path('matriculas/', include('matriculas.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('financeiro/', include('financeiro.urls')),
]
