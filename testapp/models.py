from django.db import models

# Create your models here.
from django.urls import reverse


class Company(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    ceo=models.CharField(max_length=64)

    def get_absolute_url(self):
      return reverse('details',kwargs={'pk':self.pk})
