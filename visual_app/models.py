from django.db import models


# Create your models here.
class FaceImage(models.Model):
    name = models.CharField(max_length=50)
    face_img = models.ImageField(upload_to='images/')
