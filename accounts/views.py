from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from watch.models import profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        user = User.objects.all()

        for i in user:
            if i.email == request.POST['email']:
                return render(request,'blogapp/home.html',{'error1':'Email Already Exist.'})
    try:
        user = User.objects.get(username=request.POST['username'])
        return render(request,'blogapp/home.html',{'error1':'Username Already Exist.'})

    except:
        if request.POST['password'] != request.POST['password1']:
            return render(request, 'blogapp/home.html', {'error1': "Password Does't Match."})

        else:
            user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                username=request.POST['username'],
                password=make_password(request.POST['password'])
            )
            auth.login(request,user)
            pro = profile()
            if request.FILES :
                pro.image = request.FILES['image']
            pro.profile_discreption = request.POST['profile_discreption']
            pro.user = user
            pro.save()
    return redirect(request.META.get('HTTP_REFERER'))


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user:
            auth.login(request,user)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request,'blogapp/home.html',{'error':"Username or Password Does't Exist..."})
@login_required
def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER'))