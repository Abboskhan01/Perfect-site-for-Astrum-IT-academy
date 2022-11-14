from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'index.html')


def meetings(request):
    return render(request, 'meetings.html')


def meetings_details(request):
    return render(request, 'meeting-details.html')
