
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$',view.new),
    url(r'^create/$',views.create),
    url(r'^(?P<number>\d+)/$',views.show),
    url(r'^(?P<number>\d+)/$',views.edit),
    url(r'^(?P<number>\d+)/$',views.destroy)
]