from django.shortcuts import render,HttpResponse,redirect
import traceback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.


@login_required(login_url='login')
def Homepage(request):
    return render(request,'housr_elevate_home.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('housr_elevate_app:housr_elevate_home')
        else:
            return HttpResponse('Username or Password is incorrect')

# def get_success_url(request):
#     next_url = request.GET.get('next')
#     if next_url:
#         return next_url
#     return reverse_lazy('housr_elevate_app:home')

        

    return render(request,'login.html')

def SignUpPage(request):
    try:
        print('hellooooooooo worldddddd')
        if request.method=='POST':
            uname = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1 != pass2:
                return HttpResponse("your password and Confirm Password does not match")
            elif ' ' in uname:
                return HttpResponse("Blank space not allowed in username")
            else:
                my_user = User.objects.create_user(uname,email,pass1,is_staff = True)
                
                my_user.save()
                return redirect('login')

        return render(request,'signup.html')
    except Exception as e:
        traceback.print_exc(e)

def LogoutPage(request):
    logout(request)
    return redirect('login')




