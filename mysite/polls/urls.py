from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    # pk is the expected key b/c this is what the DetailView generic expects
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # to highlight the behavior of what happens when not following the PRG pattern for form submissions
    path(
        "<int:question_id>/vote-without-redirect/",
        views.vote_without_redirect,
        name="vote_without_redirect",
    ),
]
