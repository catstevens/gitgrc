from django.conf.urls import patterns, url
from itms import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),)
