from django.urls import path
from . import views

app_name="jobs"
urlpatterns = [
    path("", views.home, name='home'),
    path('all/', views.ListAllJobsView.as_view(), name="all_jobs")
]
