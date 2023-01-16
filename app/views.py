from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhanu(request,name):
    return HttpResponse(f'i am {name}.hii...everyone')