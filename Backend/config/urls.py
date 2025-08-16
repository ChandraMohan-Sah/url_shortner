from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('apps.home.api.urls')),
    path('admin/', admin.site.urls),
    path('app1_shortner/v1/', include('apps.app1_shortner.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
