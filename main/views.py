from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mog.models import Mog 


# Homepage
# @login_required
def home(request):
    return redirect('main:dashboard')


# Dashboard
@login_required
def dashboard(request):
    user_profile = request.user.profile


    context = {
        'user_profile': user_profile,
    }
    return render(request, 'main/dashboard.html', context)


# @login_required
def all_mog(request):
    query_set = Mog.objects.all()

    context = {
        'obj_list': query_set,
    }

    return render(request, 'main/all_mog.html', context)