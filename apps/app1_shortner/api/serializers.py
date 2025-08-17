# serializers.py
from rest_framework import serializers
from app1_shortner.models import tbl_URL_Shortner


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_URL_Shortner
        fields = ['id', 'long_url', 'short_url', 'created_at']

    def validate_long_url(self, value):  
        # Check URL scheme
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                "URL must start with 'http://' or 'https://'."
            )
        
        # Check if URL already exists
        if tbl_URL_Shortner.objects.filter(long_url=value).exists():
            raise serializers.ValidationError("This URL already exists.")
        return value
    

    def create(self, validated_data):
        return tbl_URL_Shortner.objects.create(**validated_data)


