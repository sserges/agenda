from django.conf.urls import url

from .views import create, details

urlpatterns = [
    url(r'^create/$', create),
    url(r'^(\d+)/details/$', details),
]