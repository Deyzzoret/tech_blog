from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
# Create your models here.

class Author (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    slug = models.SlugField(default=None,null=True)

    def url_redirect(self):
        return reverse('post-author', kwargs={'slug':self.slug})


class TechPost (models.Model):
    title_post = models.CharField(max_length=100)
    date_post = models.DateField()
    content_post = models.CharField(max_length=500)
    image_post = models.ImageField(upload_to="images")
    authors = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="techposts")


class CommentTechPost(models.Model):
    title_comment = models.CharField(max_length=100)
    date_comment = models.DateField()
    content_comment = models.CharField(max_length=500)
    id_techpost = models.CharField(max_length=2,default="")
    posts = models.ForeignKey(TechPost,null=True,on_delete=models.CASCADE, related_name="comments")
