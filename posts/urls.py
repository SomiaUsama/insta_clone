from django.urls import path

from . import views
app_name = 'posts'

urlpatterns = [
    path("", views.LoginPage, name="login"),
    path("signup/", views.SignupPage, name="signup"),
    path("home/", views.HomePage, name="home"),
    path("logout/", views.Logout, name="logout")
    
]
