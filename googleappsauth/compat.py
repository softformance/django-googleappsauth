import django

if django.VERSION < (1, 7, 0):
    from django.contrib.auth.models import SiteProfileNotAvailable

if django.VERSION >= (1, 7, 0):
    class SiteProfileNotAvailable(Exception):
        pass

def is_authenticated(user):
    try:
        return user.is_authenticated()  # Django<1.10
    except TypeError:
        return user.is_authenticated  # Django>=1.10