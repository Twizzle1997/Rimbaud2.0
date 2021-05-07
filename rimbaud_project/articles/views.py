from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<div style="background-color:red"><b>Salut salut je suis un retour http</b></div>')

def toto(request):
    return HttpResponse('<div style="width:200px; height:200px; background-color:green"></div>')