from django import forms

from .models import *
import django_filters
import datetime


LEVEL_CHOICES = [
    ('Fabric', 'Fabric'),
    ('Cutting', 'Cutting'),
]

fabric = Fabric.objects.all()
cutting = Cutting.objects.order_by('cutting_type').values_list('cutting_type', flat=True).distinct()
worker = Worker.objects.all()

FABRIC_CHOICES = [(f.fabric_name, f.fabric_name) for f in fabric]
GLOVES_CHOICES = [(cutting[i], cutting[i]) for i in range(cutting.count())]
WORKER_CHOICES = [(w.name, w.name) for w in worker]

cur_year = datetime.datetime.today().year
year_range = tuple([i for i in range(cur_year - 2, cur_year + 1)])


class VarianceFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=year_range))
    name = django_filters.ChoiceFilter(choices=WORKER_CHOICES)
    fabric_name = django_filters.ChoiceFilter(choices=FABRIC_CHOICES)

    class Meta:
        model = Variance
        fields = ['date', 'name', 'fabric_name']


class ViewEntryFilter(django_filters.FilterSet):
    level = django_filters.ChoiceFilter(choices=LEVEL_CHOICES)
    fabric_name = django_filters.ChoiceFilter(choices=FABRIC_CHOICES)
    cutting_type = django_filters.ChoiceFilter(choices=GLOVES_CHOICES)
    name = django_filters.ChoiceFilter(choices=WORKER_CHOICES)
    date = django_filters.DateFilter(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=year_range))

    class Meta:
        model = StockEntry
        fields = ['level', 'fabric_name', 'cutting_type', 'name', 'date']


class WorkerFilter(django_filters.FilterSet):

    class Meta:
        model = Worker
        fields = ['level', 'name']