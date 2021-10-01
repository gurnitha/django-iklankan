# apps/main/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Nama halaman: home_page
def home_page(request):
	return HttpResponse('Hello World!')