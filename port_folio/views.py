from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    courses = Project.objects.all()
    return render(request,'port_folio/home.html',{'courses':courses})
