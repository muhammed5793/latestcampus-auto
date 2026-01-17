from django.urls import path
from .views import (
    StudentDashboardView,
    ProfessorDashboardView,
    AdminDashboardView
)

urlpatterns = [
    path("student/", StudentDashboardView.as_view()),
    path("professor/", ProfessorDashboardView.as_view()),
    path("admin/", AdminDashboardView.as_view()),
]
