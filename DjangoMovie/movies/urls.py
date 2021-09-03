from django.urls import path

from . import views


urlpatterns = [
    path("", views.MoviesVies.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movies_detail")
]
