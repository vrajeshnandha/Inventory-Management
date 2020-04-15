from homesite.models import *


def stock_entry(level, fabric_type, glove_type, name, quantity, date):
    if level == 'Fabric':
        glove_type = "NA"

    elif level == 'Raw_material':
        glove_type = "NA"
        name = "NA"

    entry = StockEntry(level=level, fabric_name=fabric_type, cutting_type=glove_type, name=name, quantity=quantity, date=date)
    entry.save()


def add_raw_material(fabric_type, quantity):
    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    fabric.quantity = q + quantity
    fabric.save()


def fabric_computation(fabric_type, quantity):
    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    if q < quantity:
        return 0
    fabric.quantity = q - quantity
    fabric.save()


def cutting_computation(fabric_type, glove_type, quantity):
    try:
        cutting = Cutting.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Cutting.DoesNotExist:
        return 0

    cutting.quantity = cutting.quantity + quantity
    cutting.save()


def sewing_computation(fabric_type, glove_type, quantity):
    try:
        sewing = Sewing.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Sewing.DoesNotExist:
        return 0

    try:
        cutting = Cutting.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Cutting.DoesNotExist:
        return 0

    q = cutting.quantity
    if q < quantity:
        return 1

    sewing.quantity = sewing.quantity + quantity
    cutting.quantity = q - quantity
    sewing.save()
    cutting.save()


def packing_computation(fabric_type, glove_type, quantity):
    try:
        packing = Packing.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Packing.DoesNotExist:
        return 0

    try:
        sewing = Sewing.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Sewing.DoesNotExist:
        return 0

    q = sewing.quantity
    if q < quantity:
        return 1

    packing.quantity = packing.quantity + quantity
    sewing.quantity = q - quantity
    packing.save()
    sewing.save()


def calculate_variance(name, date, fabric_type, glove_type, quantity):
    entry = StockEntry.objects.get(name=name, date=date, level="Fabric", fabric_name=fabric_type)
    given_weight = entry.quantity

    cutting = Cutting.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    w = cutting.weight
    actual_weight = quantity * (w / 1000)
    var = given_weight - actual_weight

    variance = Variance(date=date, name=name, fabric_name=fabric_type, variance=round(var, 3))
    variance.save()

    return var


def add_wages(quantity, name, level):
    worker = Worker.objects.get(name=name, level=level)
    rate = worker.rate
    balance = worker.balance
    wages = rate*quantity
    worker.balance = balance + wages
    worker.save()


def delete_entry(entry_id):
    try:
        entry = StockEntry.objects.get(entry_id=entry_id)
    except StockEntry.DoesNotExist:
        return 0

    entry.delete()
    return 1


def add_payment(name, amount):

    payment = Payment(name=name, amount=amount)
    payment.save()

    worker = Worker.objects.filter(name=name)
    if worker.count() > 1:
        if worker[0].balance > worker[1].balance:
            w = Worker.objects.get(name=name, level=worker[0].level)
            w.balance = w.balance - amount
            w.save()

        else:
            w = Worker.objects.get(name=name, level=worker[1].level)
            w.balance = w.balance - amount
            w.save()

    else:
        worker = Worker.objects.get(name=name)
        worker.balance = worker.balance - amount
        worker.save()


def invoice_compute(fabric_type, glove_type, quantity):
    try:
        packing = Packing.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Packing.DoesNotExist:
        return 0

    q = packing.quantity
    if q < quantity:
        return 1

    packing.quantity = q - quantity
    packing.save()


def invoice_entry(invoice_no, fabric_type, glove_type, quantity, date):
    entry = Invoice(invoice_no=invoice_no, fabric_name=fabric_type, cutting_type=glove_type, quantity=quantity, date=date)
    entry.save()
