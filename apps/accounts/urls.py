from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('relatorio_despesas/', views.relatorio, name='relatorio_despesas'),
    path('page-one/', views.page_one, name='page-one'),
]
