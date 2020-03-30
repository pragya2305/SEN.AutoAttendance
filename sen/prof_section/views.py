from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
import hashlib
from . import models

no = 0
qrCodeStayTime = 10000
reloadTime = 10 * 60 * 1000

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index/')
            else:
                message="Invalid username or password."
                return render(request = request,
                    template_name = "prof_section/login.html",
                    context={"form":form,
                            "message":message})
        else:
            message= "Invalid username or password."
            return render(request = request,
                    template_name = "prof_section/login.html",
                    context={"form":form,
                            "message":message})
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "prof_section/login.html",
                    context={"form":form})

@login_required(login_url='/login')
def index(request):

    username = request.user
    prof_obj = models.Prof.objects.filter(user__username = username)
    courses  = prof_obj[0].courses.split(",")
    
    context ={
            "time" : qrCodeStayTime, 
            "courses" : courses,
            "reloadTime": reloadTime
    }

    return render(request,"prof_section/index.html",context)


def getqr(request):
    
    course = request.GET["course"]
    no = random.randint(0,299)

    
    
    data={
        "no" : course+str(no),
    }
    
    return JsonResponse(data)



