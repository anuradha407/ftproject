from django.shortcuts import render
from .models import Job,Hub
# Create your views here.
def index(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
def ind(request):
         hubs=Hub.objects
         return render(request,'jobs/home.html',{'hubs':hubs})
