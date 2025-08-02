from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("HOME PAGE OF DJANGO")
    return render(request,'website/index.html')

def About(request):
    return HttpResponse("ABOUT PAGE OF DJANGO")


def Contact(request):
    return HttpResponse("CONTACT PAGE OF DJANGO")