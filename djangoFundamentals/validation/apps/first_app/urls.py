from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$',views.index),
url(r'^add_new_show',views.process1),
url(r'^add',views.add),
url(r'^edit/(?P<number>\d+)$',views.edit),
url(r'^process2/(?P<number>\d+)$',views.process2),
url(r'^destroy/(?P<number>\d+)$',views.destroy)
]