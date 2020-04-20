# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import TAProfile, TeacherProfile, AdminProfile

# Register your models here.
class TAProfileInline(admin.StackedInline):
    	model = TAProfile
    	can_delete = False
    	verbose_name_plural = 'TAProfile'
    	fk_name = 'user'

class TAUserAdmin(UserAdmin):
    	inlines = (TAProfileInline, )

    	def get_inline_instances(self, request, obj=None):
        	if not obj:
            		return list()
        	return super(TAUserAdmin, self).get_inline_instances(request, obj)

class TeacherProfileInline(admin.StackedInline):
    	model = TeacherProfile
    	can_delete = False
    	verbose_name_plural = 'TeacherProfile'
    	fk_name = 'user'

class TeacherUserAdmin(UserAdmin):
    	inlines = (TeacherProfileInline, )

    	def get_inline_instances(self, request, obj=None):
        	if not obj:
            		return list()
        	return super(TeacherUserAdmin, self).get_inline_instances(request, obj)

class AdminProfileInline(admin.StackedInline):
    	model = AdminProfile
    	can_delete = False
    	verbose_name_plural = 'AdminProfile'
    	fk_name = 'user'

class AdminUserAdmin(UserAdmin):
    	inlines = (AdminProfileInline, )

    	def get_inline_instances(self, request, obj=None):
        	if not obj:
            		return list()
        	return super(AdminUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, TAUserAdmin)
admin.site.register(User, TeacherUserAdmin)
admin.site.register(User, AdminUserAdmin)
