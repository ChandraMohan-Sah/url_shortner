# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_all_data, name='fetch_all_data'),
    path('post_long_url/', views.post_long_url, name='post_long_url'),
    path('r/<path:short_url>/', views.preprocess_redirect, name='preprocess_redirect'),
    path('delete/<int:id>/', views.delete_url, name='delete-short-url'),
]

