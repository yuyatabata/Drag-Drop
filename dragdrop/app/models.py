from django.db import models

class Image(models.Model):
    image = models.FileField(upload_to='images')
    def __str__(self):
        return self.image
