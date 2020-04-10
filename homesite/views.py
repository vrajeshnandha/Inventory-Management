from django.shortcuts import render
from .computation import *
from .forms import *


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
                flag = cutting_computation(fabric_type, glove_type, quantity)
                if flag == 0:
                    msg = "Fabric is not sufficient for cutting"
                elif flag == 2:
                    msg = "Glove type is not available for that fabric"
                else:
                    add_wages(quantity, name)
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
    if request.method == 'GET':
        form = ViewEntryForm()
        return render(request, 'homesite/viewstock.html', {'form': form})

    else:
        form = ViewEntryForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            fabric_type = form.cleaned_data['fabric_type']
            glove_type = form.cleaned_data['glove_type']
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']

            stockentry = view_entry(level, fabric_type, glove_type, name, date)
            form = ViewEntryForm()
            return render(request, 'homesite/viewentry.html', {'form': form, 'stockentry': stockentry})


def deleteEntry(request):
    if request.method == 'GET':
        form = DeleteEntryForm()
        return render(request, 'homesite/deleteentry.html', {'form': form})

    else:
        form = DeleteEntryForm(request.POST)
        if form.is_valid():
            entry_id = form.cleaned_data['entry_id']
            if delete_entry(entry_id) == 0:
                msg = "entry id does not exist"
            else:
                msg = "deleted successfully"
            form = DeleteEntryForm()
            return render(request, 'homesite/deleteentry.html', {'form': form, 'msg': msg})


def worker(request):
    worker = Worker.objects.all()
    context = {'worker': worker}
    return render(request, 'homesite/worker.html', context)


def payment(request):
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, 'homesite/payment.html', {'form': form})

    else:
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            add_payment(name,amount)
            msg = "payment successful"
            form = PaymentForm()
            return render(request, 'homesite/payment.html', {'form': form, 'msg': msg})
