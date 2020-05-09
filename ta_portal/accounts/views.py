# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import formset_factory
from django.contrib.auth import update_session_auth_hash
from accounts.models import User, TAProfile, TeacherProfile, AdminProfile, Course, TAPreference, CoursePreference, TAAllotment
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
	FindCourseForm,
	TAPreferenceForm,
	CoursePreferenceForm
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
			user.role = 1
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
			user.role = 2
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

# function to display courses of a teacher
def display_courses_teacher(request):
	pk = request.user.teacher_profile.id
	courses = Course.objects.filter(teacher_id=pk)
	args = { 'courses': courses }
	return render(request, 'accounts/display_courses_teacher.html', args)

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

# find function
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

# function to get ta preference
def ta_preference(request):
	if request.method  == 'POST':
		user = request.user
		course_count = Course.objects.all().count()
		TAPrefFormSet = formset_factory(TAPreferenceForm, extra=course_count)
		formset = TAPrefFormSet(request.POST)
		if formset.is_valid():
			i = 1
			for form in formset:
				if form.is_valid():
					cd = form.cleaned_data.get('preference')
					tapreference = TAPreference.objects.create(
						ta = user.ta_profile,
						course = cd,
						preference_no = i,
					)
					tapreference.save()
					i = i + 1
		return redirect('/accounts/home')
	else:
		course_count = Course.objects.all().count()
		TAPrefFormSet = formset_factory(TAPreferenceForm, extra=course_count)
		formset = TAPrefFormSet()
		args = { 'formset': formset }
		return render(request, 'accounts/ta_preference.html', args)

# function to get course preference
def course_preference(request, id=None):
	if request.method  == 'POST':
		user = request.user
		ta_count = TAProfile.objects.all().count()
		CoursePrefFormSet = formset_factory(CoursePreferenceForm, extra=ta_count)
		formset = CoursePrefFormSet(request.POST)
		if formset.is_valid():
			i = 1
			for form in formset:
				if form.is_valid():
					cd = form.cleaned_data.get('preference')
					coursepreference = CoursePreference.objects.create(
						ta = cd,
						course = Course.objects.get(id=id),
						preference_no = i,
					)
					coursepreference.save()
					i = i + 1
		return redirect('/accounts/home')
	else:
		ta_count = TAProfile.objects.all().count()
		CoursePrefFormSet = formset_factory(CoursePreferenceForm, extra=ta_count)
		formset = CoursePrefFormSet()
		args = { 'formset': formset }
		return render(request, 'accounts/course_preference.html', args)

def gale_shapley(request):
	tas = TAProfile.objects.all()
	courses = Course.objects.all()
	ta_count = len(tas)
	course_count = len(courses)
	tapreflist = { }
	taprefs = TAPreference.objects.all()
	for tapref in taprefs:
		ta = tapref.ta
		course = tapref.course
		pref = tapref.preference_no
		ta_pref = ( ta, pref )
		tapreflist[ta_pref] = course
	coursepreflist = { }
	courseprefs = CoursePreference.objects.all()
	for coursepref in courseprefs:
		ta = coursepref.ta
		course = coursepref.course
		pref = coursepref.preference_no
		course_ta = ( course, ta )
		coursepreflist[course_ta] = pref
	freetas = tas
	freecourses = courses
	allotment = { }
	while len(freetas) > 0:
		ta = freetas[0]
		for i in range(1, course_count + 1):
			ta_i = ( ta, i )
			course = tapreflist[ta_i]
			if course in freecourses:
				allotment[course] = ta
				freetas.exclude(ta)
				freecourses.exclude(course)
			else:
				ta1 = allotment[course]
				course_ta = ( course, ta )
				course_ta1 = ( course, ta1 )
				if coursepreflist[course_ta] < coursepreflist[course_ta1] :
					allotment[course] = ta
					freetas.exclude(ta)
					freetas.insert(ta1)
	for allot in allotment:
		taallotment = TAAllotment.objects.create(
			course = allot,
			ta = allotment[allot],
		)
		taallotment.save()
	return redirect('/accounts/home')


def ta_allotment_results(request):
	allotments = TAAllotment.objects.all()
	args = { 'allotments': allotments }
	return render(request, 'accounts/allotment.html', args)
	
	
			

