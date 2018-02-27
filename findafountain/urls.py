from django.conf.urls import url
from findafountain import views

handler404 = 'views.page_not_found'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^search/$', views.search, name='search'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^register/$', views.register, name='register'),
	]
