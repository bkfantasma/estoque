from django.urls import path 
from projeto.user import views

app_name = 'user'

urlpatterns = [
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]