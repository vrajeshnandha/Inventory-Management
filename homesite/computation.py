from homesite.models import Cutting, Fabric


def fabric_computation(fabric_type, quantity):
    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    fabric.quantity = q + float(quantity)
    fabric.save()


def cutting_computation(fabric_type, glove_type, quantity, name):
    cutting = Cutting.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    q = cutting.quantity
    w = cutting.weight

    cutting.quantity = q + int(quantity)

    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    if (q - float(quantity)*(w/1000)) >= 0:
        fabric.quantity = q - float(quantity)*(w/1000)
        fabric.save()
        cutting.save()
        return 1

    else:
        return 0



