# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.models import User, TAProfile, TeacherProfile, AdminProfile, Course
from accounts.forms import (
	UserChangeForm, 
	TAProfileChangeForm, 
	TeacherProfileChangeForm, 
	AdminProfileChangeForm,
	UserForm,
	TAProfileCreationForm,
	TeacherProfileCreationForm,
	AdminProfileCreationForm,
	CourseCreationForm,
	FindTAForm,
	FindTeacherForm,
	FindCourseForm
)

# Create your views here.

# home function
def home(request):
	args = {}
	return render(request, 'accounts/home.html', args)

# profile function
def profile(request):
	args = {}
	return render(request, 'accounts/profile.html', args)

# profile view function
def profile_view(request):
	user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile_view.html', args)

# function to view profile of others
def profile_view_other(request, pk):
	teacher = TeacherProfile.objects.get(id=pk)
	args = {'teacher': teacher}
	return render(request, 'accounts/profile_view_teacher.html', args)

# profile edit function
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

# change password function
@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/accounts/profile/view')
		else:
			return redirect('/accounts/change_password')
	else:
		form = PasswordChangeForm(user=request.user)

		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)

# add function
def add(request):
	args = {}
	return render(request, 'accounts/add.html', args)

# add ta function
def add_ta(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = TAProfileCreationForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.save()
			user.ta_profile.phone_number = profile_form.cleaned_data.get('phone_number')
			user.ta_profile.address = profile_form.cleaned_data.get('address')
			user.ta_profile.save()
			return redirect('/accounts/home')
		else:
			return redirect('/accounts/add')

	else:
		user_form = UserForm()
		profile_form = TAProfileCreationForm()
		args = {'form': user_form, 'profile_form': profile_form}
		return render(request, 'accounts/add_people.html', args)

# add teacher function
def add_teacher(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = TeacherProfileCreationForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.save()
			user.teacher_profile.phone_number = profile_form.cleaned_data.get('phone_number')
			user.teacher_profile.address = profile_form.cleaned_data.get('address')
			user.teacher_profile.save()
			return redirect('/accounts/home')
		else:
			return redirect('/accounts/add')

	else:
		user_form = UserForm()
		profile_form = TeacherProfileCreationForm()
		args = {'form': user_form, 'profile_form': profile_form}
		return render(request, 'accounts/add_people.html', args)

# add course function
def add_course(request):
	if request.method == 'POST':
		form = CourseCreationForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('/accounts/home')
		else:
			return redirect('/accounts/add')

	else:
		form = CourseCreationForm()
		args = {'form': form}
		return render(request, 'accounts/add_course.html', args)

# display function
def display(request):
	args = {}
	return render(request, 'accounts/display.html', args)

# display courses function
def display_courses(request):
	courses = Course.objects.all()
	args = { 'courses': courses }
	return render(request, 'accounts/display_courses.html', args)

# display tas function
def display_tas(request):
	tas = TAProfile.objects.all()
	args = { 'tas': tas }
	return render(request, 'accounts/display_tas.html', args)

# display teachers function
def display_teachers(request):
	teachers = TeacherProfile.objects.all()
	args = { 'teachers': teachers }
	return render(request, 'accounts/display_teachers.html', args)

def find(request):
	if request.method  == 'POST':
		ta_form = FindTAForm(request.POST)
		teacher_form = FindTeacherForm(request.POST)
		course_form = FindCourseForm(request.POST)
		if ta_form.is_valid():
			ta = ta_form.cleaned_data.get('ta')
			args = { 'ta': ta }
			return render(request, 'accounts/profile_view_ta.html', args)
		elif teacher_form.is_valid():
			teacher = teacher_form.cleaned_data.get('teacher')
			args = { 'teacher': teacher }
			return render(request, 'accounts/profile_view_teacher.html', args)
		elif course_form.is_valid():
			course = course_form.cleaned_data.get('course')
			args = { 'course': course }
			return render(request, 'accounts/view_course.html', args)
	else:	
		ta_form = FindTAForm()
		teacher_form = FindTeacherForm()
		course_form = FindCourseForm()
		args = { 'ta_form': ta_form, 'teacher_form': teacher_form, 'course_form': course_form }
		return render(request, 'accounts/find.html', args)

