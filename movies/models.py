from django.db import models
from datetime import datetime

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateTimeField(default=datetime.now(),blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Movies'