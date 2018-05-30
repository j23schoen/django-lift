import django
from django.conf import settings
import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.config.settings')

def pytest_configure():
    # settings.DEBUG = False
    settings.configure()
    django.setup()