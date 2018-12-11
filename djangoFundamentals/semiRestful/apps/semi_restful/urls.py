from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^new$',views.new),
url(r'^add$',views.add),
url(r'^show$',views.show),
url(r'^edit/(?P<number>\d+)$',views.edit),
url(r'^append/(?P<number>\d+)$',views.append),
url(r'^delete/(?P<number>\d+)$',views.destroy),
]