# apps/main/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from apps.main.models import SliderTop, Kategori

# Create your views here.

# Nama halaman: home_page
def home_page(request):
	
	slider_tops = SliderTop.objects.all()
	kategori = Kategori.objects.all()

	context = {
		'slider_tops':slider_tops,
		'kategori':kategori,
	}
	return render(request, 'main/index.html', context)