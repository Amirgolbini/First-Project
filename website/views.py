from django.shortcuts import render
from django.http import HttpResponse


def http_test(request):
    return HttpResponse("Hello")

# Create your views here.