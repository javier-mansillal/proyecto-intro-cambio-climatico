from django.http import HttpResponse

def paginaInicio(request):
    return HttpResponse("<p style='color: red;'>Bienvenido a la página web del proyecto de introducción a la ingeniería del grupo \"Jinetes del Apocalipsis\"<p>")

