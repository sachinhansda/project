# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	args = {}
	return render(request, 'accounts/home.html', args)
