from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import authenticate, login, logout

from web_project.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('starting-page')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object

        login(self.request, user)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = static('images/person.png')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        context['profile_image'] = profile_image

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete.html'
