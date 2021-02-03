from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_home_page(request):
    return HttpResponse('<h2>App is working!</h2>')