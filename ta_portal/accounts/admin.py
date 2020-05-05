# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, TAProfile, TeacherProfile, AdminProfile, Course, TAPreference, CoursePreference

# Register your models here.
"""
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
"""

admin.site.register(User)
admin.site.register(TAProfile)
admin.site.register(TeacherProfile)
admin.site.register(AdminProfile)
admin.site.register(Course)
admin.site.register(TAPreference)
admin.site.register(CoursePreference)
