from django.urls import path
from . import views
urlpatterns = [
    path("techpost/author/<slug:author>", views.TechPostAuthortView.as_view(),name="post-author"),
    path("techpost/<int:pk>", views.TechPostView.as_view()),
    path("create-techpost/", views.CreateTechPostView.as_view()),
    path("create-techpost-author/", views.CreateTechPostAuthorView.as_view()),
    path("", views.TechPostListView.as_view()),

]
