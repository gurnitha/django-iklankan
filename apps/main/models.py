# apps/main/models.py

# Django modules
from django.db import models

# Create your models here.

# Nama model: SliderTop
class SliderTop(models.Model):
	slider_title = models.CharField(
		max_length=200,
		blank=False,
		null=False)
	link = models.CharField(
		max_length=200,
		blank=False,
		null=False)
	image = models.ImageField(
		blank=True, null=True,
		upload_to='slider-top/images')

	class Meta:
		verbose_name = 'Slider top'
		verbose_name_plural = 'Sliders top'

	def __str__(self):
		return self.slider_title


# Nama model: Kategori
class Kategori(models.Model):
	nama_kategori = models.CharField(
		max_length=200, 
		blank=False,
		null=False,
		help_text='Field ini tidak boleh dikosongkan')
	slug = models.SlugField(
		max_length=100,
		unique=True,
		help_text='Field ini terisi secara otomatis')
	fa_class = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		help_text='Field ini tidak boleh dikosongkan')

	class Meta:
		verbose_name = 'Kategori'
		verbose_name_plural = 'Kategori'

	def __str__(self):
		return self.nama_kategori






