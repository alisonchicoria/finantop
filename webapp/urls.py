from django.conf.urls import url
from . import views
from django.http import HttpResponse


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^account/', views.accounts, name='accounts'),
	url(r'^users/$', views.users, name='users'),
	url(r'^hist/', views.hist, name='hist'),
	url(r'^cadastro/', views.cadastro, name='cadastro'),
	url(r'^cadastro_proc/', views.cadastro_proc, name='cadastro_proc'),
	url(r'^login/', views.login, name='login'),
	url(r'^logout/', views.logout_user, name='logout')
	]
