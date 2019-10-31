from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import ProfileRegistrationForm


def register(request):
    return render(request, "accounts/register.html", {registerform})

def add_profile(request):

    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request('Your profile is successfully registered'))
            return redirect('add_profile')
        else:
            messages.error(request('Error, your profile has not been registerd, please try again'))
            return render(request, "posts/post_list.html", {'form': form})

    else:
        form = ProfileRegistrationForm()
    return render(request, "posts/post_list.html", {'form': form})
