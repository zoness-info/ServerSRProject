# Packing/middleware.py
from threading import local
from django.utils.deprecation import MiddlewareMixin

_user = local()

class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _user.value = request.user
        print(f"CurrentUserMiddleware: process_request called, user: {_user.value}")

def get_current_user():
    user = getattr(_user, 'value', None)
    print(f"get_current_user: {user}")
    return user