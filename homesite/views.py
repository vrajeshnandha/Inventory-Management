from django.shortcuts import render
from .computation import *
from homesite.models import Cutting, Fabric


def home(request):
    return render(request, 'homesite/base.html')


def addStock(request):
    level = request.POST.get('level')
    fabric_type = request.POST.get('fabric_type')
    glove_type = request.POST.get('glove_type')
    print(glove_type)
    name = request.POST.get('name')
    quantity = request.POST.get('quantity')

    fabric = Fabric.objects.all()
    cutting = Cutting.objects.all()
    context = {'fabric': fabric, 'cutting': cutting}

    if level == "Cutting":
        level_1(fabric_type, glove_type, quantity, name)

    return render(request, 'homesite/index.html',context)


def viewStock(request):
    return render(request, 'homesite/viewstock.html')


def view(request):
    level = request.POST.get('level')

    if level == 'Fabric':
        fabric = Fabric.objects.all()
        context = {'fabric': fabric}
        return render(request, 'homesite/fabric.html', context)

    elif level == 'Cutting':
        cutting = Cutting.objects.all()
        context = {'cutting': cutting}
        return render(request, 'homesite/cutting.html', context)
