# apps/main/admin.py

# Django module
from django.contrib import admin

# Locals
from apps.main.models import (
	SliderTop,
	Kategori,
	Iklan)  

# Register your models here.

admin.site.register(SliderTop)

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
	list_display = ['nama_kategori', 'slug']
	prepopulated_fields = {'slug': ('nama_kategori',)}

@admin.register(Iklan)
class IklanAdmin(admin.ModelAdmin):
	list_display = ['nama_iklan', 'slug']
	prepopulated_fields = {'slug': ('nama_iklan',)}