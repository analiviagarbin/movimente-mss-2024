from django.urls import path
from . import views

urlpatterns = [
    path('', views.jogador_list, name='jogador_list'),  # Lista jogadores

    # Jornador
    path('register/', views.jogador_register, name='jogador_register'),  # Registro
    path('login/', views.jogador_login, name='jogador_login'),  # Login
    path('logout/', views.jogador_logout, name='jogador_logout'),  # Logout
    path('menu/', views.menu, name='menu'),  # Menu

    # Jornada
    path('jornadas/', views.listar_jornadas, name='listar_jornadas'),  # Listar jornadas
    path('jornadas/criar/', views.criar_jornada, name='criar_jornada'),  # Criar jornada
]
