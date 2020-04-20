# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal
from django.contrib.auth.models import User
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
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='ta_profile')
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

class TeacherProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='teacher_profile')
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

class AdminProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='admin_profile')
	phone_number = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, **kwargs):
    	if instance.role==1:
        	TAProfile.objects.create(user=instance)
    		instance.ta_profile.save()
    	elif instance.role==2:
        	TeacherProfile.objects.create(user=instance)
    		instance.teacher_profile.save()
    	elif instance.role==3:
        	AdminProfile.objects.create(user=instance)
    		instance.admin_profile.save()
