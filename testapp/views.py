from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from testapp.models import UserDetails
from django.views.generic import ListView
from testapp.serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.


def index(request):
    if request.method == "POST":
        Name=request.POST.get("Name")
        print(Name)
    return render(request,"testapp/index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("index")
    else:
        form=UserCreationForm()
    return render(request,"testapp/register.html",{"form":form})

# def userform(request):
#     if request.method == "POST":
#         name=request.POST.get("Name")
#         Address=request.POST.get("Address")
#         Email=request.POST.get("email")
#         Language=request.POST.getlist("language[]")
#         Birthday=request.POST.get("birthday")
#         Gender=request.POST.get("gridRadios")
#         District=request.POST.get("district")
#         Id=request.POST.get("zip")
#         print(name)
#         print(Address,District,Id)
#         print(Email)
#         for l in Language:
#             print(l)
#         print(Birthday)
#         print(Gender)
#     return render(request,"testapp/userform.html")

def userform(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        Address = request.POST.get("Address")
        Email = request.POST.get("email")
        Language = request.POST.getlist("language[]")
        Birthday = request.POST.get("birthday")
        Gender = request.POST.get("gridRadios")
        District = request.POST.get("district")
        Id = request.POST.get("zip")
        user_detail = UserDetails.objects.create(vchr_name = name, vchr_address = Address, vchr_email = Email, vchr_languages = Language, dat_dob = Birthday, vchr_gender = Gender )
        # post.save()
        return render(request,"testapp/userform.html")
    else:
        return render(request,"testapp/userform.html")

class UserList(ListView):
    model = UserDetails
