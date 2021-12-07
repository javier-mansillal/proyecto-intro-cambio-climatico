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
    quehacer =open("../proyectointro/proyectointro/plantillas/quehacer.html", encoding="utf-8")
    template1= Template(quehacer.read())
    quehacer.close()
    context1=Context()
    documento1 = template1.render(context1)
    return HttpResponse(documento1)

def cambioClimatico(request):
    return HttpResponse("<p style='color: red;'>Aquí va la información del cambio climático.<p>")

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