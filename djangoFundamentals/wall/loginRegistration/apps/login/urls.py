from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$',views.index),
url(r'^register$',views.register),
url(r'^login',views.login),
url(r'^welcome$',views.welcome),
url(r'^message$',views.message),
url(r'^comment$',views.comment),
url(r'^logout$',views.logout)
]