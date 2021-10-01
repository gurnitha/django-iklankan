# apps/main/urls.py


# Django modules
from django.urls import path

# Locals
from apps.main.views import home_page 

# App name
app_name = 'main'

urlpatterns = [
    path('', home_page, name='home_page'),
]
