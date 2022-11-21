from django.db import models

# Create your models here.

class Author (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    slug = models.SlugField(default=None,null=True)

class TechPost (models.Model):
    title_post = models.CharField(max_length=100)
    date_post = models.DateField()
    authors = models.CharField(max_length=100)
    content_post = models.CharField(max_length=500)
    image_post = models.ImageField(upload_to="images")
