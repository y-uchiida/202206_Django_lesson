from django.shortcuts import render

from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView, LogoutView
 
from .forms import MyUserCreationForm
from .forms import LoginAuthenticationForm

class AccountCreateView(generic.CreateView):
    Model = User
    form_class = UserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/accounts_create"

# 自作のフォームを利用するパターン
class AccountCreateViewUsingMyForm(generic.CreateView):
    Model = User
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = "/accounts/accounts_create_with_form"

# カスタムユーザーモデル用のログインビューのクラスを作成
class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginAuthenticationForm
 
class Logout(LogoutView):
    next_page = '/accounts/login'
 
class Home(generic.TemplateView):
    template_name = 'accounts/home.html'
