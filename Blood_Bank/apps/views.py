from .models import user
from django.shortcuts import render
from django.db.models import Q


from django.shortcuts import  render, redirect
from  .models import *

from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def firstpage(request):
    return  render(request,"firstpage.html")
def login_request(request):
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        usercheck=user.objects.get(pk=email)
        if(usercheck.email==email and usercheck.password==password):
            messages.success(request,"wellcome here")
            return render(request,"homepage.html")
        else:
            messages.error(request,"Invalid Email Or Password")
            return  render(request,"firstpage.html")


def register_request(request):
   return  render(request,"register.html")
def whyblood(request):
    return  render(request,"whyblood.html")
def eligibility(request):
    return  render(request,"eligibility.html")
def tips(request):
    return  render(request,"tips.html")
def happen(request):
    return  render(request,"happen.html")
def donarlist(request):
     donar=user.objects.all()
     return  render(request,"donarlist.html",{'donar':donar})
      #return  render(request,"donarlist.html")




def search(request):
    qur=request.POST.get('search')
    match=user.objects.filter(Q(name__icontains=qur)|Q(sel2__icontains=qur)|Q(email__icontains=qur) | Q(sel1__icontains=qur)).distinct()
     #match=user.objects.filter(email__contains=qur)
    return  render(request,"search.html",{'ab':match})
def o_positive(request):
     qur="O+"
     match=user.objects.filter(Q(sel2__icontains=qur)).distinct()
     #match=user.objects.filter(email__contains=qur)
     if(match):
       return  render(request,"O+.html",{'ab':match})
     else:
         messages.error(request,"No such donar found !")
         return  render(request,"O+.html")


def o_negative(request):
    qur = "O-"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "O-.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "O-.html")


def a_positive(request):
    qur = "A+"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "A+.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "A+.html")


def a_negative(request):
    qur = "A-"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "A-.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "A-.html")


def b_positive(request):
    qur = "B+"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "B+.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "B+.html")


def b_negative(request):
    qur = "B-"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "B-.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "B-.html")




def ab_positive(request):
    qur = "AB+"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "AB+.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "AB+.html")


def ab_negative(request):
    qur = "AB-"
    match = user.objects.filter(Q(sel2__icontains=qur)).distinct()
    # match=user.objects.filter(email__contains=qur)
    if (match):
        return render(request, "AB-.html", {'ab': match})
    else:
        messages.error(request, "No such donar found !")
        return render(request, "O-.html")


def saveinfo(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password=request.POST.get('password')
        number = request.POST.get('number')
        sel1 = request.POST.get('sel1')
        sel2 = request.POST.get('sel2')
         #a=user.objects.filter(pk='email').exists()
        # books = user.objects.get(email)


        #if(len(password)<5):


          #  messages.error(request,"Password must be at least 5 characters long")
            #return render(request,"register.html")
           # return  HttpResponse(a)

        #entry = user.objects.get(pk=email)
       # if some_queryset.filter(pk=entry.pk).exists():
        a=int(1)
        if(user.objects.filter(pk=email).exists()):
           a=0
           messages.error(request,"The email already taken. Use another email")
        if(len(password)<5):
            a=0
            messages.error(request,"The password must be at least 5 character long")
        if(a==0):
            return render(request,"register.html")
        else:
            donar_details = user(name=name, email=email, password=password,number=number, sel1=sel1, sel2=sel2)
            donar_details.save()

            messages.success(request,"Registration is successfully completed")
            #return  render(request,"firstpage.html")
            return render(request,"firstpage.html")