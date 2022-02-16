from django.shortcuts import render,get_object_or_404
from .models import Home,About,Profile
from .models import Services
from .models import Portfolio

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def index(request):

    home = Home.objects.latest('updated')
    context = {
         'home': home
         }




    return render(request, 'index.html',context)






def about(request):
      
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    context = {
      
        'about': about,
        'profiles': profiles
        

    }


    return render(request,"about.html",context)

    



def services(request):
    services = Services.objects.latest('updated')
    
    context = {
         'services': services
         }
    return render(request,"services.html",context)




def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios

        }
    return render(request,"portofilo.html",context)


def contact(request):

    return render(request,"contact.html")







