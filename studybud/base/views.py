from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('HOME PAGE')

def room(request):
    return HttpResponse('room page')