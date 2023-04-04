from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.LoginUserView.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('terms-and-conditions', views.terms, name='terms'),
    path('profile/', views.profile, name='profile')
]
