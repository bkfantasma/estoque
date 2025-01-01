from django.urls import path
from projeto.vendas import views

app_name = 'vendas'

urlpatterns = [
    path('register_venda/', views.register_venda, name='register_venda'),
    path('gerar_recibo/<int:venda_id>/', views.gerar_recibo, name='gerar_recibo'), 
]