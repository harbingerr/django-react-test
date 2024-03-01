from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(default="", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
