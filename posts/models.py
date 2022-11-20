from django.db import models

# Create your models here.

class Author (models.Model):
    name = models.CharField()
    age = models.IntegerField()
    email = models.CharField()
    address = models.CharField()

class TechPost (models.Model):
    title_post = models.CharField()
    date_post = models.DateField()
    authors = models.CharField()
    content_post = models.CharField()
    image_post = models.ImageField()
