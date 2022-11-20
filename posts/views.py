from django.shortcuts import render

from .  import models
from . import forms

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# Create your views here.

class TechPostView(DetailView):
    model = models.TechPost

class TechPostListView(ListView):
    model= models.TechPost

class CreateTechPostView(CreateView):
    template_name_suffix = ""
    model = models.TechPost
    form_class = forms.TechPostForm

