from django.db import models

# Create your models here.
from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"