# thesis/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the thesis list view
    path('', views.thesis_list, name='thesis_list'),
    
    # URL pattern for the thesis detail view
    path('<int:thesis_id>/', views.thesis_detail, name='thesis_detail'),
    
    # URL pattern for the thesis search view
    path('search/', views.thesis_search, name='thesis_search'),
    
    # URL pattern for adding a comment to a thesis
    path('<int:pk>/add_comment/', views.add_comment_to_thesis, name='add_comment_to_thesis'),
]
