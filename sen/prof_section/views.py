from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
import hashlib

no = 0
qrCodeStayTime = 1000

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
                    template_name = "login.html",
                    context={"form":form,
                            "message":message})
        else:
            message= "Invalid username or password."
            return render(request = request,
                    template_name = "login.html",
                    context={"form":form,
                            "message":message})
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

@login_required(login_url='login/')
def index(request):

    if request.method == "POST":
        course = request.POST["course"]
        return render(request,"index.html",{"qr": course,"time":qrCodeStayTime})

    else:    
        return render(request,"index.html",{"qr": "","time":qrCodeStayTime})


def getqr(request):
    
    course = request.GET["course"]
    no = random.randint(0,299)

    
    
    data={
        "no" : course+str(no),
    }
    
    return JsonResponse(data)