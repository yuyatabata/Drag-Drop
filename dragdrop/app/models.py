from django.db import models

class Image(models.Model):
    image_f = models.ImageField(upload_to='../images')
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.created_at
