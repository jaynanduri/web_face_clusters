from django.db import models


# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=500)
    company_list = models.FileField(upload_to='InputFiles', null=True, verbose_name="", blank=True)
    company_name = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name
