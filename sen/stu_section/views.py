from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from prof_section.models import AttendanceRecord
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/scan')
            else:
                message="Invalid username or password."
                return render(request = request,
                    template_name = "stu_section/login.html",
                    context={"form":form,
                            "message":message})
        else:
            message= "Invalid username or password."
            return render(request = request,
                    template_name = "stu_section/login.html",
                    context={"form":form,
                            "message":message})
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "stu_section/login.html",
                    context={"form":form})



@login_required(login_url='/login')
def scan(request):
    return render(request,"stu_section/scan.html")


def test(request):
    
    qr = request.POST['qr']
    usernm = request.user
    
    attRec = AttendanceRecord()
    attRec.studentID = usernm
    attRec.courseID = qr
    attRec.dateTime = datetime.now()

    
    attRec.save()
    
    data={
        "message":"done"
    }
    return JsonResponse(data)