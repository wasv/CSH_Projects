from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import *


# Checks if user has a profile
def profile_check(user):
    return user.is_authenticated() and hasattr(user, 'profile')


def loginTest(request):
    if request.user.is_authenticated():
        return render(request,'errorView.html',{'error_msg':"You are logged in as: "+str(request.user.username)})
    else:
        return render(request,'errorView.html',{'error_msg':"Not Logged In"})


@login_required(login_url='loginTest')
def profileCreate(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=request.user)
        if hasattr(request.user, 'profile'):
            profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        else:
            profile_form = ProfileForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
        return redirect('profileView',uname=user.username)
    else:
        user_form = UserForm(instance=request.user)
        if hasattr(request.user, 'profile'):
            profile_form = ProfileForm(instance=request.user.profile)
        else:
            profile_form = ProfileForm()
    return render(request,'profileCreate.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


@user_passes_test(profile_check, login_url='profileCreate')
def profileView(request,uname):
    user = get_object_or_404(User,username=uname)
    project_list = Project.objects.filter(owner=user.profile)
    return render(request, 'profileView.html', {'user':user,'project_list':project_list})


@user_passes_test(profile_check, login_url='profileCreate')
def projectCreate(request):
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST, files=request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.owner = request.user.profile
            project.save()
        else:
            print(project_form.errors)
        return redirect('projectView',project_id=project.id)

    else:
        project_form = ProjectForm()
    return render(request,'projectCreate.html',{'project_form':project_form})


@user_passes_test(profile_check, login_url='profileCreate')
def projectEdit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user.profile == project.owner:
        if request.method == 'POST':
            project_form = ProjectForm(data=request.POST, instance=project, files=request.FILES)
            if project_form.is_valid():
                project_form.save()
            else:
                print(project_form.errors)
            return redirect('projectView',project_id=project.id)
        else:
            project_form = ProjectForm(instance=project)
            return render(request,'projectEdit.html',{'project_form':project_form,'project':project})
    else:
        return render(request,'errorView.html',{'error_msg':"Only the project owner can edit a project."})


@user_passes_test(profile_check, login_url='profileCreate')
def projectView(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request,'projectView.html',{'project':project})


@user_passes_test(profile_check, login_url='profileCreate')
def index(request):
    project_list = Project.objects.filter(state__in=['C','O']).order_by('-last_update')[:10]
    return render(request,'projectList.html',{'project_list':project_list})


@user_passes_test(profile_check, login_url='profileCreate')
def listAll(request):
    project_list = Project.objects.order_by('-last_update')[:10]
    return render(request,'projectList.html',{'project_list':project_list})


@user_passes_test(profile_check, login_url='profileCreate')
def listActive(request):
    project_list = Project.objects.filter(state__in=['O','D']).order_by('-last_update')
    return render(request,'projectList.html',{'project_list':project_list,'title':'Active Projects'})


@user_passes_test(profile_check, login_url='profileCreate')
def listDone(request):
    project_list = Project.objects.filter(state='D').order_by('-last_update')
    return render(request,'projectList.html',{'project_list':project_list,'title':'Completed Projects'})


@user_passes_test(profile_check, login_url='profileCreate')
def listDead(request):
    project_list = Project.objects.filter(state='A').order_by('last_update')
    return render(request,'projectList.html',{'project_list':project_list,'title':'Abandoned Projects'})