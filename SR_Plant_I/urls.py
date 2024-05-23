

from django.urls import path
# from .views import MyLoginView
from .views import root_login_view
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('', root_login_view, name='login'),
     path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]

