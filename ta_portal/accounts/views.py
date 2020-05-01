# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from accounts.models import User, TAProfile, TeacherProfile, AdminProfile
from accounts.forms import UserChangeForm, TAProfileChangeForm, TeacherProfileChangeForm, AdminProfileChangeForm

# Create your views here.
def home(request):
	args = {}
	return render(request, 'accounts/home.html', args)

def profile(request):
	args = {}
	return render(request, 'accounts/profile.html', args)

def profile_view(request):
	user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile_view.html', args)

def profile_edit(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance=request.user)
		if request.user.role == 1:
			profile_form = TAProfileChangeForm(request.POST, instance=request.user.ta_profile)
		elif request.user.role == 2:
			profile_form = TAProfileChangeForm(request.POST, instance=request.user.teacher_profile)
		elif request.user.role == 3:
			profile_form = TAProfileChangeForm(request.POST, instance=request.user.admin_profile)

		if form.is_valid() and profile_form.is_valid():
			user_form = form.save()
			custom_form = profile_form.save(False)
            		custom_form.user = user_form
            		custom_form.save()
			return redirect('/accounts/profile/view')

	else:
		form = UserChangeForm(instance=request.user)
		if request.user.role == 1:
			profile_form = TAProfileChangeForm(instance=request.user.ta_profile)
		elif request.user.role == 2:
			profile_form = TeacherProfileChangeForm(instance=request.user.teacher_profile)
		elif request.user.role == 3:
			profile_form = AdminProfileChangeForm(instance=request.user.admin_profile)
		args = {'form': form, 'profile_form': profile_form}
		return render(request, 'accounts/profile_edit.html', args)
