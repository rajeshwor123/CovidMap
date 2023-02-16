from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.baseconv import base64

from .forms import PatientAdd
from .models import pandemic
from .maps import maps
import folium

# Create your views here.
def home(request):


    m = maps().map()
    m2=maps().map2()
    m3=maps().map3()
    bar=maps().bar()

    m = m._repr_html_()
    m2 = m2._repr_html_()
    m3 = m3._repr_html_()


    context = {'patientList':pandemic.objects.all(),'map':m,'map2':m2,'map3':m3,'bar':bar}
    return render(request,"home.html",context)


def patientAdd(request, id=0):
    if request.method == "GET":
        if(id == 0):
            form = PatientAdd()
        else:
            patient = pandemic.objects.get(pk=id)
            form = PatientAdd(instance=patient)
        return render(request,"patientAdd.html",{'form': form})
    else:
        if(id == 0):
            form = PatientAdd(request.POST)
        else:
            patient = pandemic.objects.get(pk=id)
            form = PatientAdd(request.POST,instance = patient)
        if form.is_valid():
            form.save()

        return redirect('home')

def patientDelete(request,id):
    patient = pandemic.objects.get(pk=id)
    patient.delete()
    return redirect('home')
