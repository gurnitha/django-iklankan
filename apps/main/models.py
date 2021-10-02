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

	class Meta:
		verbose_name = 'Slider top'
		verbose_name_plural = 'Sliders top'

	def __str__(self):
		return self.slider_title








