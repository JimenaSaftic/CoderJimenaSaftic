from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def bienvenida (request):
    return render (request, "index.html")