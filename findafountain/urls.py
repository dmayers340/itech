from django.conf.urls import url
from findafountain import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^fountain/$', views.get_fountain, name='fountain'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^register/$', views.register, name='register'),
	url(r'^submitted/$', views.submitted, name='submitted'),
	]
