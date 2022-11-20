from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User
from . import Gesture_Controller
import sys
user_id_list =[]
# Create your views here.

def User_Auth(func):
    def wrapper(*args,**kwargs):
        if not user_id_list:
            print("Not Authenticated")
            return redirect('/')
        else:
            print("Authenticated")
            return func(*args, **kwargs)
    return wrapper

def login(request):
    try:
        if request.method=="POST":
            username = request.POST.get('username')
            password=request.POST.get('password')
            userdata = User.objects.get(username=username,password=password)
            if userdata:
                user_id_list.append(userdata.id)
                request.session['id'] = userdata.id
                return redirect('/home')
    except:
        print("Error")

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_type = request.POST.get('re_password')
        userdata = User.objects.filter(username=username)
        if userdata:
            print("Username Already Exist")
        elif password != re_type:
            print("Password and confirm password does not match")
        else:
            User(username=username,password=password).save()
            return redirect('/')
    return render(request,"register.html")

@User_Auth
def home(request):
    userid = request.session['id']
    data = User.objects.get(id=userid)
    return render(request,'home.html',{'data':data})

def logout(request):
    try:
        user_id_list.pop()
        del request.session['id']
        return redirect('/')
    except:
        print("Error")

def handle(request):
    obj = Gesture_Controller.GestureController()
    obj.start()

# def stop(request):
#     sys.exit()
    
