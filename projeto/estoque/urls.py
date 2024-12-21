from django.urls import path
from projeto.estoque import views 

app_name = 'estoque'

urlpatterns = [
    path('', views.estoque_entrada_list, name='estoque_entrada_list'),
    path('saida/', views.estoque_saida_list, name='estoque_saida_list'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),  
    path('saida/add/', views.estoque_saida_add, name='estoque_saida_add'),  
    path('entrada/<int:pk>/', views.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('saida/<int:pk>/', views.estoque_saida_detail, name='estoque_saida_detail'),
    path('estoque/baixa/', views.dar_baixa_estoque_add, name='dar_baixa_estoque_add'),
    path('estoque/baixa/saida', views.dar_baixa_estoque_saida, name='dar_baixa_estoque_saida'),
]