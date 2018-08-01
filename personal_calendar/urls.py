from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_event, name="list_event"),
    url(r'^create/$', views.create_event, name="create_event"),
    url(r'^(\d+)/update/$', views.update_event, name="update_event"),
    url(r'^(\d+)/details/$', views.event_details, name="event_details"),
    url(r'^(\d+)/delete/$', views.delete_event, name="delete_event"),
    url(r'^(\d+)/participant/(\d+)/delete/$', views.delete_participant, name="delete_participant"),
]