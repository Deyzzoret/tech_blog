from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect
from django.utils.text import slugify
from django.urls import reverse

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
        form.instance.slug = slugify(form.instance.name + form.instance.age)
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

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        # Adding to the context the comment form to be displayed
        commentForm = forms.CommentForm()
        commentForm.fields["id_techpost"].initial  = self.get_object().pk
        context['commentform'] = commentForm

        context["related_comments"] = len(models.TechPost.objects.get(pk=int(self.get_object().pk)).comments.all())
        context['comments_query_set'] = models.TechPost.objects.get(pk=int(self.get_object().pk)).comments.all()

        favoriteTechPost = self.request.session.get('favoritechposts', [])
        context['isfavorite'] = True if self.get_object().pk in favoriteTechPost else False

        return context
    

class TechPostListView(ListView):
    template_name= "posts/all_techposts.html"
    model= models.TechPost

class CreateTechPostView(CreateView):
    template_name = "posts/create_post.html"
    model = models.TechPost
    form_class = forms.TechPostForm
    success_url = "/create-techpost/"

    def form_valid(self, form):
            print(type(form))
            # print(dir(form))
            valueSelectedAuthor = form.cleaned_data['author_id']
            authorObj = models.Author.objects.get(id=int(valueSelectedAuthor))

            form.instance.authors = authorObj
            self.object = form.save()
            # do something with self.object
            # remember the import: from django.http import HttpResponseRedirect
            return HttpResponseRedirect(self.get_success_url())


"""Function views"""

def addCommentToTechPost(request):
    if request.method == "POST":
        objCommentFrom = forms.CommentForm(request.POST)
        # idTechPost = request.POST['id_techpost']
        # title_comment = request.POST['title_comment']
        # date_comment = request.POST['date_comment']
        # content_comment = request.POST['content_comment']
        if objCommentFrom.is_valid():
            objTechPost = models.TechPost.objects.get(pk=int(objCommentFrom.cleaned_data['id_techpost']))
            objCommentFrom.instance.posts=objTechPost
            objCommentFrom.save()

            return HttpResponseRedirect(reverse("datailed-techpost",kwargs={
                'pk':int (objCommentFrom.cleaned_data['id_techpost'])
            }))

def addTechPostFavorites(request):
    if request.method == "POST":
        idtechpost = int(request.POST["idtechpost"])
        favoriteTechPost = request.session.get('favoritechposts', [])

        favoriteTechPost.append(idtechpost)

        print(favoriteTechPost)
        request.session['favoritechposts'] = favoriteTechPost
        request.session.modified = True

        # return HttpResponseRedirect(reverse("thanks-page"))

        return HttpResponseRedirect(reverse("datailed-techpost",kwargs={
                'pk':idtechpost
            }))

def thanks_page(request):
    return render(request,'posts/thanks.html')


        
        







