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


class ViewStockForm(forms.Form):
    level = forms.CharField(widget=forms.Select(choices=LEVEL_CHOICES))


class AddStockForm(forms.Form):
    level = forms.CharField(widget=forms.Select(choices=LEVEL_CHOICES))
    fabric_type = forms.CharField(widget=forms.Select(choices=FABRIC_CHOICES))
    glove_type = forms.CharField(widget=forms.Select(choices=GLOVES_CHOICES))
    name = forms.CharField(widget=forms.Select(choices=WORKER_CHOICES))
    quantity = forms.FloatField()


# solve this issue
class DeleteEntryForm(forms.Form):
    # entry = StockEntry.objects.all()
    # ENTRY_CHOICES = [(i.entry_id, i.entry_id) for i in entry]
    entry_id = forms.CharField()


class ViewEntryForm(forms.Form):
    cur_year = datetime.datetime.today().year
    year_range = tuple([i for i in range(cur_year - 2, cur_year + 1)])
    level = forms.CharField(widget=forms.Select(choices=[('', '---SELECT ONE---'), ] + LEVEL_CHOICES), required=False)
    fabric_type = forms.CharField(widget=forms.Select(choices=[('', '---SELECT ONE---'), ] + FABRIC_CHOICES), required=False)
    glove_type = forms.CharField(widget=forms.Select(choices=[('', '---SELECT ONE---'), ] + GLOVES_CHOICES), required=False)
    name = forms.CharField(widget=forms.Select(choices=[('', '---SELECT ONE---'), ] + WORKER_CHOICES), required=False)
    date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=year_range), required=False)


class PaymentForm(forms.Form):
    name = forms.CharField(widget=forms.Select(choices=WORKER_CHOICES))
    amount = forms.FloatField()
