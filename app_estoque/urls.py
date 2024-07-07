from django.urls import path
from app_estoque import views
from django.contrib import admin

urlpatterns = [
   path('', views.home, name ='home'),
   path('produtos/', views.listagem_produtos, name='listagem_produtos'),
   path('criar_produtos/', views.criar_produtos, name='criar_produtos'),
   path('produtos/<int:produto_id>/deletar/', views.deletar_produto, name='deletar_produto'),
   path('produtos/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
   path('login/', views.user_login, name='app_login'),
   path('logout/', views.user_logout, name='app_logout'),
   path('register/', views.register_user, name='register'),
]


