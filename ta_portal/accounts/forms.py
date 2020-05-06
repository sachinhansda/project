from django import forms
from django.db import models
from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, TAProfile, TeacherProfile, AdminProfile, Course

class UserChangeForm(ModelForm):
	class Meta:
		model = User
		fields = (
			'email',
		)

class TAProfileChangeForm(ModelForm):
	class Meta:
		model = TAProfile
		fields = (
			'phone_number',
			'address',
		)

class TeacherProfileChangeForm(ModelForm):
	class Meta:
		model = TeacherProfile
		fields = (
			'phone_number',
			'address',
		)

class AdminProfileChangeForm(ModelForm):
	class Meta:
		model = AdminProfile
		fields = (
			'phone_number',
			'address',
		)

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user


class TAProfileCreationForm(ModelForm):
	class Meta:
		model = TAProfile
		fields = (
			'phone_number',
			'address',
		)

class TeacherProfileCreationForm(ModelForm):
	class Meta:
		model = TeacherProfile
		fields = (
			'phone_number',
			'address',
		)

class AdminProfileCreationForm(ModelForm):
	class Meta:
		model = AdminProfile
		fields = (
			'phone_number',
			'address',
		)

class CourseCreationForm(ModelForm):
	class Meta:
		model = Course
		fields = (
			'course_id',
			'name',
			'department',
			'credits',
			'students',
			'teacher',
			'course_type',
		)

class FindTAForm(Form):
	ta = forms.ModelChoiceField(queryset=TAProfile.objects.all())

class FindTeacherForm(Form):
	teacher = forms.ModelChoiceField(queryset=TeacherProfile.objects.all())

class FindCourseForm(Form):
	course = forms.ModelChoiceField(queryset=Course.objects.all())

class TAPreferenceForm(Form):
	preference = forms.ModelChoiceField(queryset=Course.objects.all())

class CoursePreferenceForm(Form):
	preference = forms.ModelChoiceField(queryset=TAProfile.objects.all())
