from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

# ログイン用の処理 =======
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = "accounts/login.html"

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "accounts/login.html"