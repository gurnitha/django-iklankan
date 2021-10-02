# apps/main/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from apps.main.models import (
	SliderTop, 
	Kategori,
	Iklan)

# Create your views here.

# Nama halaman: home_page
def home_page(request):
	
	# Semua SliderTop
	slider_tops = SliderTop.objects.all()
	# Semua Kategori
	kategori = Kategori.objects.all()
	# Semua Iklan dgn klasifikasi terpopuler
	iklan_terpoputer = Iklan.objects.filter(klasifikasi='Terpopuler')
	print(iklan_terpoputer)
	context = {
		'slider_tops':slider_tops,
		'kategori':kategori,
		'iklan_terpoputer':iklan_terpoputer,
	}
	return render(request, 'main/index.html', context)