# proyek/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # main app
    path('', include('apps.main.urls', namespace='main')),

    # admin app 
    path('admin/', admin.site.urls),
]
