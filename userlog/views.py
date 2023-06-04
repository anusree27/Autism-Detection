from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import joblib
import numpy as np


# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url="login")
def home(request):
    return render(request,"home.html")
    
def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    context = {'page': page}
    return render(request, "login_register.html", context)


def logoutPage(request):
    logout(request)
    return redirect("/")


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            print(user)

            if user is not None:
                login(request, user)
                return redirect("/")

    context = {"form": form, "page": page}
    return render(request, "login_register.html", context)


   
def result(request):
    lis=[]
    lis.append(request.GET['hiddenq1'])
    lis.append(request.GET['hiddenq2'])
    lis.append(request.GET['hiddenq3'])
    lis.append(request.GET['hiddenq4'])
    lis.append(request.GET['hiddenq5'])
    lis.append(request.GET['hiddenq6'])
    lis.append(request.GET['hiddenq7'])
    lis.append(request.GET['hiddenq8'])
    lis.append(request.GET['hiddenq9'])
    lis.append(request.GET['hiddenq10'])
    lis.append(request.GET['age'])
    lis.append(request.GET['gender'])
    lis.append(request.GET['ethnicity'])
    lis.append(request.GET['hidden_jaun'])
    lis.append(request.GET['hidden_pdd'])
    lis.append(request.GET['country'])
    lis.append(request.GET['hidden_screen'])
    lis.append(request.GET['total_score_hidden'])
    lis.append(request.GET['who'])
    print(lis)
    tot=lis[17]
    loaded_model=joblib.load('model.pkl')
    arr=np.array(lis)
    nm=arr.reshape(1,19)
    a=loaded_model.predict(nm)
    return render(request,"result.html",{'ans':a,'total':tot})