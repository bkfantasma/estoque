import django
from django.apps import apps
from django.conf import settings

django.setup()

apps.populate(settings.INSTALLED_APPS)
