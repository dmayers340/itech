from django.conf.urls import url
from waterfountain import views

handler404 = 'views.page_not_found'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^findafountain/$', views.findafountain, name='findafountain'),

	]
