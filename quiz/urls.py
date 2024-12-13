from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.user_login, name="login"),  # Root URL shows the login page
    path("logout/", views.user_logout, name="logout"),
    path("start/", views.start_quiz, name="start"),
    path("form/", views.form_questions, name="form_questions"),
    path("submit/", views.submit_answers, name="submit_answers"),
    path("results/", views.results, name="results"),
]
