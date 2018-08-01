from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

from .views import create_account

urlpatterns = [
    url(r'^create_account/$', create_account, name="create_account"),
    url(r'^succes/$', TemplateView.as_view(template_name="user/succes.html"), name="succes"),
    url(r'^login/$', login, {'template_name':'user/login.html'}, name="login"),
    url(r'^logout/$', logout, {'next_page':'/user/login/'}, name="logout"),
    url(
        r'^profile/$',
        login_required(TemplateView.as_view(template_name="user/profile.html")),
        name="profile"
    ),
]