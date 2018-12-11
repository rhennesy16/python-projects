from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$',views.index),
url(r'^register$',views.register),
url(r'^login$',views.login),
url(r'^jobs$',views.jobs),
url(r'^new$',views.new),
url(r'^add$',views.add),
url(r'^show/(?P<number>\d+)$',views.show),
url(r'^edit/(?P<number>\d+)$',views.edit),
url(r'^append/(?P<number>\d+)$',views.append),
url(r'^delete/(?P<number>\d+)$',views.destroy),
url(r'^logout$',views.logout)
]