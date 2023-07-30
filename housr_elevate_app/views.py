from django.shortcuts import redirect, render, get_object_or_404 , HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required , permission_required
from loginsys.models import Resident, CommunityEvent
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
# @login_required(login_url='login')
def Homepage(request):
    # return HttpResponse('WELCOME')
    # user = authenticate(request,username=request.GET.username,password=request.GET.pass1)
    # if user is not None:
    #         login(request,user)
    return render(request,'housr_elevate_home.html')



@csrf_exempt
# @login_required(login_url='login')
# @permission_required()
def Resident_all_listing(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2222222222222222222222")

    Lisitng = Resident.objects.all()

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2222222222222222222222")
    return HttpResponse('WELCOME')
    # return render('housr_elevate_app:resident_listing',{'listing':Lisitng})






    



