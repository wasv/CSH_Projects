from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import *


# Checks if user has a profiles
def profile_check(user):
    return user.is_authenticated() and hasattr(user, 'profile')


def loginTest(request):
    if request.user.is_authenticated():
        return HttpResponse("You are logged in as:",str(request.user.username))
    else:
        return HttpResponse("Not logged in")


@user_passes_test(profile_check, login_url='loginTest')
def setupProfile(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=request.user)
        if hasattr(request.user, 'profile'):
            profile_form = ProfileForm(data=request.POST, instance=request.user.profile)
        else:
            profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm(instance=request.user)
        if hasattr(request.user, 'profile'):
            profile_form = ProfileForm(instance=request.user.profile)
        else:
            profile_form = ProfileForm()
    return render(request,'setupProfile.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


@user_passes_test(profile_check, login_url='loginTest')
def newProject(request):
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
        project = project_form.save(commit=False)
        project.owner = request.user.profile
        project.save()

    else:
        project_form = ProjectForm()
    return render(request,'newProject.html',{'project_form':project_form})


@user_passes_test(profile_check, login_url='loginTest')
def index(request):
    project_list = Project.objects.all();
    return render(request,'listProjects.html',{'project_list':project_list})
