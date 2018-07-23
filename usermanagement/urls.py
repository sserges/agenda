from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^succes/$', TemplateView.as_view(template_name="user/succes.html")),
]