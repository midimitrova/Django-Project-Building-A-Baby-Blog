
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import authenticate, login, logout

from web_project.accounts.forms import RegisterUserForm, UserEditForm


UserModel = get_user_model()


class RegisterUserView(views.CreateView):
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
        context['posts_count'] = self.object.post_set.count()

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit.html'
    model = UserModel
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('profile-details-user', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('starting-page')
