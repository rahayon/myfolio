from django import urls
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
# Create your models here.
class MyService(models.Model):

    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=300,blank=True)
    description = models.TextField(blank=True)
    service_image = models.ImageField(upload_to="service/")


    class Meta:
        verbose_name = "My Service"
        verbose_name_plural = "My Services"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

    def imageURL(self):
        try:
            url = self.service_image.url
        except:
            url = ''

        return url

class MyProject(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    project_url = models.URLField(max_length=200, blank=True)
    project_image = models.ImageField(upload_to="service/", blank=True)

    class Meta:
        verbose_name = "MyProject"
        verbose_name_plural = "MyProjects"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("MyProject_detail", kwargs={"pk": self.pk})

    
    def imageURL(self):
        try:
            url = self.project_image.url
        except:
            url = ''

        return url
