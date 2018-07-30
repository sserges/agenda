from django.conf.urls import url

from .views import create, details, delete_participant

urlpatterns = [
    url(r'^create/$', create),
    url(r'^(\d+)/details/$', details),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete_participant),
]