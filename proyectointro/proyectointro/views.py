from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from apps.metano.models import Metano
from apps.co2.models import Co2

def paginaInicio(request):
    return render(request, "home.html", {})

def ong(request):
    return render(request, "ong.html", {})

def dioxidoCarbono(request):
    dioxidoLista = Co2.objects.all()
    nombres = []
    for i in dioxidoLista:
        nombres.append(i.actividad)
    set(nombres)
    return render(request, "co2.html", {"actividades": nombres, "listaDioxido": dioxidoLista})

def metano(request):
    metanoLista = Metano.objects.all()
    return render(request, "metano.html", {"listaMetano": metanoLista})

def valparaiso(request):
    return render(request, "valparaiso.html", {})

def queHacer(request):
    quehacer =open("../proyectointro/proyectointro/plantillas/quehacer.html", encoding="utf-8")
    template1= Template(quehacer.read())
    quehacer.close()
    context1=Context()
    documento1 = template1.render(context1)
    return HttpResponse(documento1)

def cambioClimatico(request):
    return render(request, "cambio_climatico.html", {})

def politica(request):
    politica =open("../proyectointro/proyectointro/plantillas/politica.html", encoding="utf-8")
    template2= Template(politica.read())
    politica.close()
    context2=Context()
    documento2 = template2.render(context2)
    return HttpResponse(documento2)

def agua(request):
    agua =open("../proyectointro/proyectointro/plantillas/agua.html", encoding="utf-8")
    template3= Template(agua.read())
    agua.close()
    context3=Context()
    documento3 = template3.render(context3)
    return HttpResponse(documento3)

def compostaje(request):
    compostaje =open("../proyectointro/proyectointro/plantillas/compostaje.html", encoding="utf-8")
    template4= Template(compostaje.read())
    compostaje.close()
    context4=Context()
    documento4 = template4.render(context4)
    return HttpResponse(documento4)

def encuesta(request):
    return render(request,'encuesta.html',{})