from django.urls import path
from projeto.produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
    path('add/', views.ProdutoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit/', views.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/deletar/', views.produto_delete, name='produto_delete'),
    path('<int:pk>/json/', views.produto_json, name='produto_json'),
]