from django.shortcuts import render

from .models import JobsConfig
# Create your views here.
def home(request):
    jobs = JobsConfig.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
