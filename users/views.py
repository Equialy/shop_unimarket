from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from products.models import BasketUser
from users.forms import LoginForm, SignUpForm, ProfileForm




# Create your views here.
class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    extra_context = {'title': 'Авторизация'}





class SignUpUser(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/sign_up.html'
    extra_context = {'title': 'Регистрация'}
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)





class Profile( LoginRequiredMixin,UpdateView):
    form_class = ProfileForm
    template_name = 'users/profile_user.html'
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = BasketUser.objects.filter(user=self.request.user)
        return context




# def sign_up(request):
#     if request.method == "POST":
#         form_register = RegisterUserForm(request.POST)
#         if form_register.is_valid():
#             user = form_register.save(commit=False)
#             user.set_password(form_register.cleaned_data['password'])
#             user.save()
#             return render(request, 'users/success_sign_up.html')
#     else:
#
#         form_register = RegisterUserForm()
#     data = {
#         'form_register': form_register
#     }
#     return render(request, 'users/sign_up.html', data)
