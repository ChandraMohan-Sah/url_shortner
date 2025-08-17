# urls.py
from django.urls import path
from . import views

urlpatterns = [ 
    path('create_list/short-url/', views.ShortenedURLListCreateView.as_view(), name='short-url-list-create'),
    path('delete/<int:id>/', views.ShortenedURLDeleteView.as_view(), name='short-url-delete'),
    path('redirect/<str:short_code>/', views.ShortURLRedirectView.as_view(), name='short-url-redirect'),
]
