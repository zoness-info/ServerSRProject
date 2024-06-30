

from django.urls import path
# from .views import MyLoginView
from .views import root_login_view
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', root_login_view, name='login'),

     path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)