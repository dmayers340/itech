from django.conf.urls import url
from findafountain import views

handler404 = 'views.page_not_found'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^map/$', views.map, name='map'),
	url(r'^search/$', views.search, name='search'),
	url(r'^contact/$', views.contact, name='contact'),
	]
