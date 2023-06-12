from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .forms import Registration
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Logout(request):
    logout(request)
    messages.success(request,"Logout Done")
    return redirect("Home")

def Login(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully")
                return redirect("Home")
            else:
                messages.error(request,"No User Found")
        else:
            messages.error(request,"Invalid Data")
    else:
        messages.error(request,"Must Need to Login")
        form = AuthenticationForm()
    context ={
        'form':form
    }
    return render(request,"login.html",context)

def signup(request):

    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
        else:
            messages.error(request,"Something Wrong")
    else:
        form = Registration()
    context = {
        "form":form,
    }
        
    return render(request,"signup.html",context)

