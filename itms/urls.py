from django.conf.urls import patterns, url
from itms import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),
		url(r'^login/$', views.login, name='login'),)
