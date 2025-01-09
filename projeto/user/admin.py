from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'nome',
        'sobrenome',
        'email',
        'cpf',
        'password',
    )
