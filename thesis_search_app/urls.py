# thesis_search_app/urls.py
from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('thesis/', include('thesis.urls')),  
]