from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def create_profile(request):
    return HttpResponse("HI there")
