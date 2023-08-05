from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import authenticate, login, logout

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    pass


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'



class LogoutUserView(auth_views.LogoutView):
    pass
