from django.db import models


class MyPhoto(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='Images/', default='Images/None/No-img.jpg')
    doc = models.FileField(upload_to='Doc/', default='Doc/None/No-doc.pdf')
