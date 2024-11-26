from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_views, name='home'),
    path('home-logado', views.homelogado_views, name='home_logado'),
    path('tratamentos/', include('tratamentos.urls')),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('gerenciar-medicos/', views.gerenciar_medicos, name='gerenciar_medicos'),
    path('adicionar-medico/', views.add_medico, name='adicionar_medico'),
    path('remover-medico/<int:medico_id>/', views.remover_medico, name='remover_medico'),
    path('resetar-senha-medico/<int:medico_id>/', views.resetar_senha_medico, name='resetar_senha_medico'),
    path('medico_login/', views.medico_login, name='medico_login'),
    path('medico-home/', views.medico_home, name='medico_home'),
    path('agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('minhas-consultas/', views.minhas_consultas, name='minhas_consultas'),
]