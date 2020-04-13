from django import forms
from .models import Fabric, Cutting, Worker
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


class ViewStockForm(forms.Form):
    level = forms.CharField(widget=forms.Select(choices=LEVEL_CHOICES))


class AddStockForm(forms.Form):
    level = forms.CharField(widget=forms.Select(choices=[('Raw_material', 'Raw Material'), ] + LEVEL_CHOICES))
    fabric_type = forms.CharField(widget=forms.Select(choices=FABRIC_CHOICES))
    glove_type = forms.CharField(widget=forms.Select(choices=GLOVES_CHOICES))
    name = forms.CharField(widget=forms.Select(choices=WORKER_CHOICES))
    quantity = forms.FloatField()
    date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget(years=year_range))


# solve this issue
class DeleteEntryForm(forms.Form):
    # entry = StockEntry.objects.all()
    # ENTRY_CHOICES = [(i.entry_id, i.entry_id) for i in entry]
    entry_id = forms.CharField()


class PaymentForm(forms.Form):
    name = forms.CharField(widget=forms.Select(choices=WORKER_CHOICES))
    amount = forms.FloatField()
