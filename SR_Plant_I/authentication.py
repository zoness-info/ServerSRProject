from django.contrib.auth import authenticate

def custom_authenticate(username, password):
    return authenticate(username=username, password=password)