from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginTest(request):
    if request.user.is_authenticated():
        return HttpResponse(request.user.username)
    else:
        return HttpResponse("Not logged in")