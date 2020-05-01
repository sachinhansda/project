from django import forms
from django.forms import ModelForm
from accounts.models import User, TAProfile, TeacherProfile, AdminProfile

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
