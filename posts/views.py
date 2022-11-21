from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect
from django.utils.text import slugify

from .  import models
from . import forms

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# Create your views here.

"""
AUTHOR
"""
class TechPostAuthortView(DetailView):
    template_name= "posts/detail_techpost_author.html"
    model = models.Author

    def get_queryset(self):
        try:
            return super().get_queryset()
        except:
            raise Http404()

class CreateTechPostAuthorView(CreateView):
    template_name = "posts/create_author.html"
    model = models.Author
    form_class = forms.AuthorForm
    success_url = "/create-techpost-author/"

    def form_valid(self, form):
        print(type(form))
        # print(dir(form))
        form.instance.slug = slugify(form.instance.name)
        self.object = form.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())



"""
TECHPOST
"""

class TechPostView(DetailView):
    template_name= "posts/detail_techpost.html"
    model = models.TechPost

    def get_queryset(self):
        try:
            return super().get_queryset()
        except:
            raise Http404()
    

class TechPostListView(ListView):
    template_name= "posts/all_techposts.html"
    model= models.TechPost

class CreateTechPostView(CreateView):
    template_name = "posts/create_post.html"
    model = models.TechPost
    form_class = forms.TechPostForm
    success_url = "/create-techpost/"





