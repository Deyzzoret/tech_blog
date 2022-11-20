from django.urls import path
from . import views
urlpatterns = [
    path("techpost/<int:pk>", views.TechPostView().as_view()),
    path("create", views.CreateTechPostView.as_view()),
    path("", views.TechPostListView().as_view()),

]
