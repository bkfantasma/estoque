from django.urls import path
from projeto.fornecedores import views      

app_name = 'fornecedores'

urlpatterns = [
    path('', views.fornecedor, name='fornecedor'),
    path('add/', views.fornecedor_add, name='fornecedor_add'),
    path('editar/<int:pk>/', views.fornecedor_edit, name='fornecedor_edit'),
    path('delete/<int:pk>/', views.fornecedor_delete, name='fornecedor_delete'),
]
