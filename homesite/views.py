from django.shortcuts import render
from .computation import *


def index(request):
    level = request.POST.get('level')
    fabric_type = request.POST.get('fabric_type')
    glove_type = request.POST.get('glove_type')
    name = request.POST.get('name')
    quantity = request.POST.get('quantity')

    if level == "1":
        level_1(fabric_type, glove_type, quantity, name, 0.320)

    return render(request, 'homesite/index.html')
