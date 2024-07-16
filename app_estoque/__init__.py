import django
from django.apps import apps
from django.conf import settings

# Certifique-se de que settings.INSTALLED_APPS está configurado corretamente
django.setup()

apps.populate(settings.INSTALLED_APPS)
