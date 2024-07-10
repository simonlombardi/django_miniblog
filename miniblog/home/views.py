from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout)
from users.forms import UserRegisterForm

class LoginView(View):

    def get(self, requests):
        return render(
            requests,
            'home/login.html'
        )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request,
                                username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form':form
            }  
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'form':form
            }
        )

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@login_required(login_url='login')
def index_view(request):
    return render(
        request,
        'home/index.html'
    )
