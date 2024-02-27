from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.thesis_list, name='thesis_list'),
    
    path('<int:thesis_id>/', views.thesis_detail, name='thesis_detail'),
    
    path('search/', views.thesis_search, name='thesis_search'),

    path('<int:pk>/add_comment/', views.add_comment_to_thesis, name='add_comment_to_thesis'),
]
