from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm


# Create your views here.
def loginTest(request):
    if request.user.is_authenticated():
        return HttpResponse(str(request.user))
    else:
        return HttpResponse("Not logged in")


@login_required(login_url='loginTest')
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
