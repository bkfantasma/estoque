from django.urls import path
from app_estoque import views

urlpatterns = [
   path('', views.home, name ='home'),
   path('produtos/', views.listagem_produtos, name='listagem_produtos'),
   path('criar_produtos/', views.criar_produtos, name='criar_produtos'),
   path('produtos/<int:produto_id>/deletar/', views.deletar_produto, name='deletar_produto'),
   path('produtos/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),
]
