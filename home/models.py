import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    messagge = models.TextField()

class gallery1 (models.Model):
    gallery_typename = models.CharField(max_length=30)
    typename_bgpic = models.ImageField(upload_to="static/gallerypic")

    def __str__(self):
        return self.gallery_typename

class gallery_subitem (models.Model):
    subitem_img = models.ImageField(upload_to="static/sub_gallery")
    image_name = models.CharField (max_length=40, default=False, null=True)
    gallery1 = models.ForeignKey (gallery1, on_delete=models.CASCADE,default=False, null=True)

    def __str__(self):
        return self.image_name





