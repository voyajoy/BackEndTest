from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^commits/?$', views.filter_commits),
    url(r'^commits/(?P<sha>\w{40})/?$', views.commit),
]
