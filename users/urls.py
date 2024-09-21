
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'users'




urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign_up/', views.SignUpUser.as_view(), name='sign_up'),
    path('profile/', views.Profile.as_view(), name='profile_user'),


]
