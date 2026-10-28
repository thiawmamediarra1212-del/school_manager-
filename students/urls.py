from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("apropos/", views.about, name="about"),
    path("etudiants/", views.student_list, name="student_list"),
    path("enseignants/", views.teacher_list, name="teacher_list"),
    path("etudiants/<int:id>/", views.student_detail, name="student_detail"),
]
