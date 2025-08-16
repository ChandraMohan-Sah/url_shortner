from django.db import models
from django.utils import timezone
import uuid

class tbl_URL_Shortner(models.Model):
    short_url = models.CharField(
        max_length=15, 
        unique=True, 
        db_index=True
    )
    long_url = models.URLField()
    expiracy = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.expiracy

    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"

