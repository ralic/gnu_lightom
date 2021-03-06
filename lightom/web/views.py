from django.shortcuts import render
from .models import Concentrador, Dispositivo


def concentradores(request):
    concentradores = Concentrador.objects.order_by('serial')
    context = {'concentradores':concentradores}
    return render(request, "web/concentrador.html", context)


def dispositivos(request, pk):
    dispositivos = Dispositivo.objects.filter(concentrador=pk)
    context = {'dispositivos':dispositivos}
    return render(request, "web/dispositivo.html", context)
