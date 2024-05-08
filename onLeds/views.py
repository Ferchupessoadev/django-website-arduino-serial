from time import sleep

import serial
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

ser = serial.Serial("/dev/ttyUSB0", 57600, timeout=1)


# Create your views here.
def index(request):
    return render(request, "index.html")


def orden(request, orden):
    ser.write(orden.encode("ascii"))
    if orden == "p":
        message = "Timbre encendido"
    elif orden == "n":
        message = "Timbre apagado"
    return JsonResponse({"message": message})
