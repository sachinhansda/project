from django.conf.urls import url
from . import views
from django.contrib.auth.views import ( 
	login, 
	logout, 
	password_reset, 
	password_reset_done,
	password_reset_confirm,
	password_reset_complete
)

urlpatterns = [
	url(r'^home/$', views.home, name='home'),
    	url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile/view/$', views.profile_view, name='profile_view'),
	url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
	url(r'^change_password/$', views.change_password, name='change_password'),
	url(r'^add/$', views.add, name='add'),
	url(r'^add/ta/$', views.add_ta, name='add_ta'),
	url(r'^add/teacher/$', views.add_teacher, name='add_teacher'),
	url(r'^add/course/$', views.add_course, name='add_course'),

    	url(r'^reset_password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    url(r'^reset_password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset_password/complete/$', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')
]    
