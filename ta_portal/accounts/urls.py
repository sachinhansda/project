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
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile/view/$', views.profile_view, name='profile_view'),
	url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
	url(r'^change_password/$', views.change_password, name='change_password')
]    
