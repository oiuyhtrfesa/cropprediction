from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from .forms import CropParametersForm
from .models import CropParametersCollect
# Create your views here. user-anusha password-123
def HomePage(request):
    return render(request,'home1.html')
def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pasw1=request.POST.get('password1')
        pasw2=request.POST.get('password2')
        user=authenticate(request,username=uname,password=pasw1)
        if pasw1!=pasw2:
            return HttpResponse("Your password and conform password are not same")
        elif user is not None:
            return HttpResponse("User existed.....try to login")
        else:
            my_user=User.objects.create_user(uname,email,pasw1)
            my_user.save()
            return redirect('home')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
           return HttpResponse("User name or password incorrect")
    return render(request,'login.html')

def LogOutPage(request):
    logout(request)
    return redirect('login')

def getPredictions(N,P,K,temperature,humidity,ph,rainfall):
    import pickle
    model=pickle.load(open(rb"D:\ml dl\crop_detection\crop_prediction_web\crop_prediction_web\crop_model.sav","rb"))
    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    return (prediction)
def index(request):
    return render(request,'index.html')

def result(request):
    N=int(request.GET['N'])
    P=int(request.GET['P'])
    K=int(request.GET['K'])
    temperature=float(request.GET['temperature'])
    humidity=float(request.GET['humidity'])
    ph=float(request.GET['ph'])
    rainfall=float(request.GET['rainfall'])
    result=getPredictions(N,P,K,temperature,humidity,ph,rainfall)
    form=CropParametersCollect(N=N,P=P,K=K,temperature=temperature,humidity=humidity,ph=ph,rainfall=rainfall,crop_type=result)
    form.save()
    return render(request,'result.html',{'result':result})

def DisplayData(request):
    crop_parameters = CropParametersCollect.objects.all()
    # for i in crop_parameters:
    #     print(i.N,i.P,i.K)
    # return render(request,'home1.html')
    return render(request, 'display_data.html', {'crop_parameters': crop_parameters})