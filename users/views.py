from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginForm, RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

def register(request):  # sourcery skip: extract-method
    template = 'users/register.html'
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have been registered successfuly")
            return redirect('jobs:home')
        else:
            messages.error(request, "Registration failed. Please try again.")
    context = {
        'form': form
    }
    return render(request, template, context)





class LoginUserView(LoginView):
    template_name = "users/login.html"
    next_page = 'jobs:home'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'You were successfully login')
        return HttpResponseRedirect(self.get_success_url())

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out successfully')

    return redirect("jobs:home")

def terms(request):
    template = 'users/terms-and-conditions.html'
    context = {}
    return render(request, template, context)

@login_required
def profile(request):
    template = 'users/profile.html'
    context = {}
    return render(request, template, context)