from django.shortcuts import render,HttpResponse
from home.models import contact

# Create your views here.


def  home(request):
    context ={"name":"Walelign","course":"Javascript"}
    return render(request, 'home.html',context)

def  about(request):
    return render(request, 'about.html')
def  project(request):
   return render(request, 'project.html')
def  contact(request):
    if request.method =="POST":
       
        email=request.POST['email']
        address=request.POST ['address']
        aboutyou=request.POST ['aboutyou']
        
        ins=contact( email=email,address=address,aboutyou=aboutyou)
        ins.save()  
    return render(request, 'contact.html')