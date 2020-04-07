from django.shortcuts import render
from .computation import *
from .models import Cutting, Fabric, StockEntry
from .forms import ViewStockForm, AddStockForm, deleteEntryForm


def home(request):
    return render(request, 'homesite/base.html')


def addStock(request):
    if request.method == 'GET':
        form = AddStockForm()
        return render(request, 'homesite/index.html', {'form': form})

    else:
        form = AddStockForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            fabric_type = form.cleaned_data['fabric_type']
            glove_type = form.cleaned_data['glove_type']
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            stock_entry(level, fabric_type, glove_type, name, quantity)

            form = AddStockForm()
            msg = ""

            if level == "Fabric":
                fabric_computation(fabric_type, quantity)

            if level == "Cutting":
                flag = cutting_computation(fabric_type, glove_type, quantity, name)
                if flag == 0:
                    msg = "Fabric is not sufficient for cutting"
                elif flag == 2:
                    msg = "Glove type is not available for that fabric"

            if msg == "":
                msg = "submission successful"

            return render(request, 'homesite/index.html', {'form': form, 'msg': msg})


def viewStock(request):
    if request.method == 'GET':
        form = ViewStockForm()
        return render(request, 'homesite/viewstock.html', {'form': form})

    else:
        form = ViewStockForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']

            if level == 'Fabric':
                fabric = Fabric.objects.all()
                context = {'fabric': fabric}
                return render(request, 'homesite/fabric.html', context)

            elif level == 'Cutting':
                cutting = Cutting.objects.all()
                context = {'cutting': cutting}
                return render(request, 'homesite/cutting.html', context)


def viewEntry(request):
    stockentry = StockEntry.objects.all()
    context = {'stockentry': stockentry}
    return render(request, 'homesite/viewentry.html', context)


def deleteEntry(request):
    if request.method == 'GET':
        form = deleteEntryForm()
        return render(request, 'homesite/deleteentry.html', {'form': form})

    else:
        form = deleteEntryForm(request.POST)
        if form.is_valid():
            entry_id = form.cleaned_data['entry_id']
            entry = StockEntry.objects.get(entry_id=entry_id)
            entry.delete()
            msg = "deleted successfully"
            form = deleteEntryForm()
            return render(request, 'homesite/deleteentry.html', {'form': form, 'msg': msg})
