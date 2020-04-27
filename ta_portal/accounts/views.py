# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	args = {}
	return render(request, 'accounts/home.html', args)

def profile_view(request):
	user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile_view.html', args)
