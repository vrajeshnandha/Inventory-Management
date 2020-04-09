from homesite.models import Cutting, Fabric, StockEntry


def stock_entry(level, fabric_type, glove_type, name, quantity):
    if level == 'Fabric':
        glove_type = "NA"

    entry = StockEntry(level=level, fabric_name=fabric_type, cutting_type=glove_type, name=name, quantity=quantity)
    entry.save()


def fabric_computation(fabric_type, quantity):
    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    fabric.quantity = q + quantity
    fabric.save()


def cutting_computation(fabric_type, glove_type, quantity, name):
    try:
        cutting = Cutting.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    except Cutting.DoesNotExist:
        return 2

    q = cutting.quantity
    w = cutting.weight

    cutting.quantity = q + quantity

    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    if (q - quantity * (w / 1000)) >= 0:
        fabric.quantity = q - quantity * (w / 1000)
        fabric.save()
        cutting.save()
        return 1

    else:
        return 0


def view_entry(level, fabric_type, glove_type, name):
    stockentry = StockEntry.objects.all()

    if level != "":
        stockentry = stockentry.filter(level=level)
    #
    if fabric_type != "":
        stockentry = stockentry.filter(fabric_name=fabric_type)

    if glove_type != "":
        stockentry = stockentry.filter(cutting_type=glove_type)

    if name != "":
        stockentry = stockentry.filter(name=name)

    return stockentry


def delete_entry(entry_id):
    try:
        entry = StockEntry.objects.get(entry_id=entry_id)
    except StockEntry.DoesNotExist:
        return 0

    entry.delete()
    return 1


