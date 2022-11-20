
from . import models
from django import forms

class TechPostForm(forms.ModelForm):
    class Meta:
        model = models.TechPost
        fields = "__all__"
