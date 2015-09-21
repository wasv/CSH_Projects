from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm


# Create your views here.
def loginTest(request):
    if request.user.is_authenticated():
        return HttpResponse(request.user.username)
    else:
        return HttpResponse("Not logged in")


@login_required(login_url='loginTest')
def setupProfile(request):

    registered= False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
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
    return render(request,'setupProfile.html')