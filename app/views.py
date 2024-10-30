from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_busname(request):
    TYU = BusForms()
    d = {'TYU':TYU}
    if request.method == 'POST':
        FGH = BusForms(request.POST)
        if FGH.is_valid():
            FGH.save()
           
            return HttpResponse('bus is inserted')
        else:
            return HttpResponse('bus is not inserted check given data is valid or not ')


    return render(request,'insert_busname.html',d)
def insert_passengers(request):
    TYUI = PassengersForms()
    d = {'TYUI':TYUI}
    if request.method == 'POST':
        FGHJ = PassengersForms(request.POST)
        if FGHJ.is_valid():
            FGHJ.save()
            return HttpResponse('passenger is inserted')
        else:
            return HttpResponse('passenger is not inserted check given data is valid or not ')
    return render(request,'insert_passengers.html',d)
