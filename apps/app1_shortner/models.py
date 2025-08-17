from django.db import models
from django.utils import timezone
import uuid

class tbl_URL_Shortner(models.Model):
    short_url = models.CharField(
        max_length=20, 
        unique=True, 
        db_index=True,
        blank=True,
    )
    long_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"


class tbl_UniqueNumberRange(models.Model):
    start = models.BigIntegerField()
    end = models.BigIntegerField()
    current = models.BigIntegerField(default=0)  # pointer to next available ID
    server_id = models.CharField(max_length=50, default="server1")

    def get_next(self):
        if self.current < self.end:
            self.current += 1
            self.save(update_fields=["current"])
            return self.current
        return None  # exhausted

 