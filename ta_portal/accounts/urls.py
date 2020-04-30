from django.conf.urls import url
from . import views
from django.contrib.auth.views import ( 
	login, 
	logout
)

urlpatterns = [
	url(r'^home/$', views.home, name='home'),
    	url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
	url(r'^profile/view/$', views.profile_view, name='profile_view')
]    