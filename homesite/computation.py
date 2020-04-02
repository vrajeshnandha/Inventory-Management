from homesite.models import Cutting, Fabric


def level_1(fabric_type, glove_type, Quantity, name, x):
    cutting = Cutting.objects.get(fabric_name=fabric_type, cutting_type=glove_type)
    q = cutting.quantity

    cutting.quantity = q + int(Quantity)
    cutting.save()

    fabric = Fabric.objects.get(fabric_name=fabric_type)
    q = fabric.quantity

    fabric.quantity = q - float(Quantity)*x
    fabric.save()


