from django.shortcuts import redirect, render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = SignupForm()

    context = {
        "form": form,
    }
    return render(request, 'authenticate/signup.html', context)



def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
