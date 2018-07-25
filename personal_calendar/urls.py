from django.conf.urls import url

from .views import create

urlpatterns = [
    url(r'^create/$', create)
]