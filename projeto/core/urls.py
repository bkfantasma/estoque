from django.urls import path
from projeto.core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_vendas', views.list_vendas, name='list_vendas'),
    path('financas/', views.financas, name='financas'),
]
