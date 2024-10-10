from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def profile(request):
    return render(request, "profile.html")


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,
                  'registration.html',
                  {'form': UserCreationForm()})

