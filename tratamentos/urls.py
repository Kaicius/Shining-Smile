from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todos', views.tratamentos_view, name='tratamentos'),
    path('ortodontia', views.ortondontia_view, name='ortodontia'),
    path('clareamento', views.clareamento_view, name='clareamento'),
    path('proteses', views.proteses_view, name='proteses'),
    path('implantes', views.implantes_view, name='implantes'),
    path('todos-logado', views.tratamentoslogado_view, name='tratamentos_logado'),
    path('ortodontia-logado', views.ortondontialogado_view, name='ortodontia_logado'),
    path('clareamento-logado', views.clareamentologado_view, name='clareamento_logado'),
    path('proteses-logado', views.proteseslogado_view, name='proteses_logado'),
    path('implantes-logado', views.implanteslogado_view, name='implantes_logado'),
]