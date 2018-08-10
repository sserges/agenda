from django.conf.urls import url
from django.views.generic.list import ListView

from . import views
from .models import Evenement

urlpatterns = [
    url(r'^$', views.list_event, name="event_home"),
    url(r'^create/$', views.create_event, name="create_event"),
    url(r'^(\d+)/update/$', views.update_event, name="update_event"),
    url(r'^(\d+)/details/$', views.event_details, name="event_details"),
    url(r'^list/$', views.list_event, name="list_event"),
    url(r'^listes/$',views.Evenement_Liste.as_view(paginate_by=3)),
    url(
        r'^listes/(?P<champ>[\w-]+)/(?P<terme>[\w-]+)/$',
        views.Evenement_Liste.as_view(paginate_by=3)
    ),
    url(r'^(\d+)/delete/$', views.delete_event, name="delete_event"),
    url(r'^(\d+)/participant/(\d+)/delete/$', views.delete_participant, name="delete_participant"),
]