from django.shortcuts import render
from .computation import *
from .forms import *
from .filters import *


def home(request):
    return render(request, 'homesite/base.html')


def addStock(request):
    if request.method == 'GET':
        form = AddStockForm()
        return render(request, 'homesite/addstock.html', {'form': form})

    else:
        form = AddStockForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            fabric_type = form.cleaned_data['fabric_type']
            glove_type = form.cleaned_data['glove_type']
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            date = form.cleaned_data['date']

            form = AddStockForm()
            msg = "submission successful"

            if level == "Raw_material":
                add_raw_material(fabric_type, quantity)

            if level == "Fabric":
                flag = fabric_computation(fabric_type, quantity)
                if flag == 0:
                    msg = "fabric is not sufficient for allocation"

            if level == "Cutting":
                flag = cutting_computation(fabric_type, glove_type, quantity)
                if flag == 0:
                    msg = "Glove type is not available for that fabric"
                else:
                    variance = calculate_variance(name, date, fabric_type, glove_type, quantity)
                    msg = "variance is: " + str(round(variance, 3)) + " kg"
                    add_wages(quantity, name, level)

            if level == "Sewing":
                flag = sewing_computation(fabric_type, glove_type, quantity)
                if flag == 0:
                    msg = "Glove type is not available for that fabric"
                elif flag == 1:
                    msg = "not sufficient material for sewing"
                else:
                    add_wages(quantity, name, level)

            if level == "Packing":
                flag = packing_computation(fabric_type, glove_type, quantity)
                if flag == 0:
                    msg = "Glove type is not available for that fabric"
                elif flag == 1:
                    msg = "not sufficient material for packing"
                else:
                    add_wages(quantity, name, level)

            if msg == "submission successful":
                stock_entry(level, fabric_type, glove_type, name, quantity, date)

            return render(request, 'homesite/addstock.html', {'form': form, 'msg': msg})


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
                table = Cutting.objects.all()
                context = {'table': table, 'info': "Cutting Stock"}
                return render(request, 'homesite/display.html', context)

            elif level == 'Sewing':
                table = Sewing.objects.all()
                context = {'table': table, 'info': "Sewing Stock"}
                return render(request, 'homesite/display.html', context)

            elif level == 'Packing':
                table = Packing.objects.all()
                context = {'table': table, 'info': "Packing Stock"}
                return render(request, 'homesite/display.html', context)


def viewEntry(request):
    entry = StockEntry.objects.all()
    entry_filter = ViewEntryFilter(request.GET, queryset=entry)
    return render(request, 'homesite/viewentry.html', {'filter': entry_filter})


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
    worker_filter = WorkerFilter(request.GET, queryset=worker)
    return render(request, 'homesite/worker.html', {'filter': worker_filter})


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


def list_variance(request):
    variance = Variance.objects.all()
    variance_filter = VarianceFilter(request.GET, queryset=variance)
    return render(request, 'homesite/variance_list.html', {'filter': variance_filter})


def add_invoice(request):
    if request.method == 'GET':
        form = InvoiceForm()
        return render(request, 'homesite/addinvoice.html', {'form': form})

    else:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            incoice_no = form.cleaned_data['invoice_no']
            fabric_type = form.cleaned_data['fabric_type']
            glove_type = form.cleaned_data['glove_type']
            quantity = form.cleaned_data['quantity']
            date = form.cleaned_data['date']

            form = AddStockForm()
            msg = "submission successful"

            flag = invoice_compute(fabric_type, glove_type, quantity)
            if flag == 0:
                msg = "Glove type is not available for that fabric"
            elif flag == 1:
                msg = "not sufficient material for delivery"

            if msg == "submission successful":
                invoice_entry(incoice_no, fabric_type, glove_type, quantity, date)

            return render(request, 'homesite/addinvoice.html', {'form': form, 'msg': msg})


def view_invoice(request):
    entry = Invoice.objects.all()
    entry_filter = ViewInvoiceFilter(request.GET, queryset=entry)
    return render(request, 'homesite/viewinvoice.html', {'filter': entry_filter})