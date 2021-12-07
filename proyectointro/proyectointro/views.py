from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from apps.metano.models import Metano

def paginaInicio(request):
    return render(request, "home.html", {})

def ong(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de ONG.<p>")

def dioxidoCarbono(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de dióxido de carbono.<p>")

def metano(request):
    metanoLista = Metano.objects.all()
    return render(request, "metano.html", {"listaMetano": metanoLista})

def valparaiso(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de Valparaíso.<p>")

def queHacer(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de ¿Qué hacer?<p>")

def cambioClimatico(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información del cambio climático.<p>")