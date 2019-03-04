import django

if django.VERSION < (1, 7, 0):
    from django.contrib.auth.models import SiteProfileNotAvailable

if django.VERSION >= (1, 7, 0):
    class SiteProfileNotAvailable(Exception):
        pass