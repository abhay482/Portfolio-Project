from django.shortcuts import render

# Create your views here.
from .models import job

def home(request):
    Jobs = job.objects
    return render(request, 'jobs/home.html', {'jobs': Jobs})
