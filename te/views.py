from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def athul(request):
    return HttpResponse('yes,iam athul')


def sag(request):
    return HttpResponse('yes,iam sagar')


