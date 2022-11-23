from django.urls import path
from . import views
urlpatterns = [
    path("techpost/author/<slug:slug>", views.TechPostAuthortView.as_view(),name="post-author"),
    path("techpost/<int:pk>", views.TechPostView.as_view(),name="datailed-techpost"),
    path("create-techpost/", views.CreateTechPostView.as_view()),
    path("create-techpost-author/", views.CreateTechPostAuthorView.as_view()),
    path("add-comment/", views.addCommentToTechPost),
    path("add-favorites/", views.addTechPostFavorites),
    path("thanks/", views.thanks_page,name="thanks-page"),
    path("", views.TechPostListView.as_view()),

]
