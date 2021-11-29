from django.http import HttpResponse
from django.template import Template, Context
def paginaInicio(request):
    plantillaInicio = open("../proyectointro/proyectointro/plantillas/home.html", encoding="utf-8")
    template = Template(plantillaInicio.read())
    plantillaInicio.close()
    context = Context()
    documento = template.render(context)
    return HttpResponse(documento)

def ong(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de ONG.<p>")

def dioxidoCarbono(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de dióxido de carbono.<p>")

def metano(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de metano.<p>")

def valparaiso(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de Valparaíso.<p>")

def queHacer(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información de ¿Qué hacer?<p>")

def cambioClimatico(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información del cambio climático.<p>")