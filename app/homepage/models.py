from django.db import models


# Create your models here.
class ApprenticeshipDevelop(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    url = models.URLField(max_length=400, default='#')
