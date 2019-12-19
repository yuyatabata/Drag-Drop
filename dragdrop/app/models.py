from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
