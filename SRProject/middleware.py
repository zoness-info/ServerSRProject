from django.contrib.auth.middleware import AuthenticationMiddleware


from threading import local
from django.utils.deprecation import MiddlewareMixin

_user = local()

class CustomMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        _user.value = request.user
        print(f"CurrentUserMiddleware: process_request called, user: {_user.value}")