from django.contrib import admin 
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('app_estoque/', include('app_estoque.urls')),
   path('accounts/', include('django.contrib.auth.urls')),

]