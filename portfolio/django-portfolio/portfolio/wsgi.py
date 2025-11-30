import os
import sys

def get_wsgi_application():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    from django.core.wsgi import get_wsgi_application
    return get_wsgi_application()

application = get_wsgi_application()