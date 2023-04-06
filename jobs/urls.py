from django.urls import path
from . import views

app_name="jobs"
urlpatterns = [
    path("home/", views.home, name='home'),
    path('all/', views.ListAllJobsView.as_view(), name="list_all_jobs")
]
