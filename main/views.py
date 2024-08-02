from django.shortcuts import render
from django.http import HttpResponse


def IndexView(request):
    return render(request, "index.html")

def Panel(request):
    return render(request, "panel.html")

def Comparendo(request):
    return render (request,"comparendo.html")

def Vehiculos(request):
    return render (request,"vehiculos.html")

def Taxis(request):
    return render (request,"taxis.html")

def Siniestros(request):
    return render (request,"siniestros.html")

def Exeptuados(request):
    return render (request,"exeptuados.html")

def Picoyplaca(request):
    return render (request,"picoyplaca.html")

def Ventanilla(request):
    return render (request,"ventanilla.html")

def Agendacita(request):
    return render (request,"agendacita.html")

