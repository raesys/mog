from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib import messages
from .forms import ProfileForm, SignUpForm
from accounts.models import Profile


# from django.contrib.auth.forms import UserCre/ationForm
# from django.urls import reverse_lazy
# from django.views import generic
# from django.contrib.auth.forms import UserCreationForm

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data.get('username')
            user_profile = Profile(user=user)
            profile_form = ProfileForm(request.POST, instance=user_profile)
            profile_form.save()
            messages.success(request, "Your account has been successfully created!")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('main:dashboard')
        else:
            messages.error(request, "Correct the errors below")
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/register.html', context)

