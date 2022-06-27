from django.shortcuts import render
from django.shortcuts import HttpResponse

def signup_view(request):
    return HttpResponse('Signup Completed!')