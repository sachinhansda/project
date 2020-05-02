# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
#from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    	TA = 1
    	TEACHER = 2
    	ADMIN = 3
    	ROLE_CHOICES = (
        	(TA, 'TA'),
        	(TEACHER, 'Teacher'),
        	(ADMIN, 'Admin'),
    	)
	role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

class TAProfile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True, related_name='ta_profile')
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

class TeacherProfile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True, related_name='teacher_profile')
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

class AdminProfile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True, related_name='admin_profile')
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, **kwargs):
    	if instance.role==1:
        	TAProfile.objects.get_or_create(user=instance)
    		instance.ta_profile.save()
    	elif instance.role==2:
        	TeacherProfile.objects.get_or_create(user=instance)
    		instance.teacher_profile.save()
    	elif instance.role==3:
        	AdminProfile.objects.get_or_create(user=instance)
    		instance.admin_profile.save()

class Course(models.Model):
	COURSE_TYPES = (
		('L','Lab'),
		('T','Theory'),
	)
	course_id = models.CharField(max_length=20)
	name = models.CharField(max_length=255)
	department = models.CharField(max_length=100)
	credits = models.IntegerField()
	students = models.IntegerField(default=0)
	teacher = models.ForeignKey(TeacherProfile, related_name='course_teacher', on_delete=models.CASCADE)
	course_type = models.CharField(max_length=1, choices=COURSE_TYPES)

class TAPreference(models.Model):
	ta = models.ForeignKey(TAProfile, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	preference_no = models.IntegerField()

class CoursePreference(models.Model):
	ta = models.ForeignKey(TAProfile, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	preference_no = models.IntegerField()

class Declaration(models.Model):
	MONTHS = (
		('Jan','January'),
		('Feb','February'),
		('Mar','March'),
		('Apr','April'),
		('May','May'),
		('Jun','June'),
		('Jul','July'),
		('Aug','August'),
		('Sep','September'),
		('Oct','October'),
		('Nov','November'),
		('Dec','December'),
	)
	APPROVALS = (
		('Y','Yes'),
		('N','No'),
	)
	month = models.CharField(max_length=3, choices=MONTHS)
	avg_hours = models.IntegerField()
	days = models.IntegerField()
	approval = models.CharField(max_length=1, choices=APPROVALS)
	rating = models.DecimalField(max_digits=3, decimal_places=2)
	ta = models.ForeignKey(TAProfile, on_delete=models.CASCADE)
