# views.py
from rest_framework import generics, status
from rest_framework.response import Response

from app1_shortner.models import tbl_URL_Shortner
from .serializers import ShortenedURLSerializer
from app1_shortner.scripts.short_url import get_short_url
from django.shortcuts import redirect, get_object_or_404

# swagger docs 
from drf_yasg.utils import swagger_auto_schema 
from django.utils.decorators import method_decorator 


@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=['🎞️ App1: URL Shortner'], operation_id='list all URLS [AllowAny]',
    operation_description='list all URLS [AllowAny]',
))
@method_decorator(name='post', decorator=swagger_auto_schema(
    tags=['🎞️ App1: URL Shortner'], operation_id='create a Short URL [AllowAny]',
    operation_description='create a Short URL  [AllowAny]',
)) 
class ShortenedURLListCreateView(generics.ListCreateAPIView):
    queryset = tbl_URL_Shortner.objects.all()
    serializer_class = ShortenedURLSerializer

    def perform_create(self, serializer):
        url_instance = serializer.save()
        short_url = get_short_url()
        url_instance.short_url = short_url
        url_instance.save()

        return Response(
            {
                "short_url": short_url, 
                "long_url": url_instance.long_url
            },
            status=status.HTTP_201_CREATED
        )



@method_decorator(name='delete', decorator=swagger_auto_schema(
    tags=['🎞️ App1: URL Shortner'], operation_id='delete a Short URL [AllowAny]',
    operation_description='delete a Short URL  [AllowAny]',
)) 
class ShortenedURLDeleteView(generics.DestroyAPIView):
    queryset = tbl_URL_Shortner.objects.all()
    lookup_field = 'id'  

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Return custom response
        return Response(
            {
                "detail": f"Short URL deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT
        )
    

@method_decorator(name='get', decorator=swagger_auto_schema(
    tags=['🎞️ App1: URL Shortner'], operation_id='redirect a Short URL [AllowAny]',
    operation_description='redirect a Short URL  [AllowAny]',
)) 
class ShortURLRedirectView(generics.RetrieveAPIView):
    """
        Redirects a short URL to its original long URL.
    """
    serializer_class = ShortenedURLSerializer
    lookup_field = 'short_code'

    def get_object(self):
        short_code = self.kwargs.get(self.lookup_field)
        return get_object_or_404(tbl_URL_Shortner,  short_url=short_code)

    def get(self, request, *args, **kwargs):
        url_instance = self.get_object()
        return redirect(url_instance.long_url)



