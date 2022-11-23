
from . import models
from django import forms

def get_authors ():
    choices_form=[]
    all_authors = models.Author.objects.all()
    for author in all_authors:
        print("Authors in DB")
        print(author.pk)
        print (author.name)
        choices_form.append((author.pk,author.name))
    return choices_form
class TechPostForm(forms.ModelForm):
    class Meta:
        model = models.TechPost
        fields = "__all__"
        exclude = ["authors"]

    author_id = forms.ChoiceField(label="Choose an author",choices=get_authors)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        exclude = ['slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentTechPost
        exclude = ['posts']
        widgets = {
            'id_techpost':forms.HiddenInput()
        }



