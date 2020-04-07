from django import forms
from .models import Fabric, Cutting, StockEntry

LEVEL_CHOICES = [
    ('Fabric', 'Fabric'),
    ('Cutting', 'Cutting'),
]

fabric = Fabric.objects.all()
cutting = Cutting.objects.order_by('cutting_type').values_list('cutting_type', flat=True).distinct()

FABRIC_CHOICES = [(f.fabric_name, f.fabric_name) for f in fabric]
GLOVES_CHOICES = [(cutting[i], cutting[i]) for i in range(cutting.count())]


class ViewStockForm(forms.Form):
    level = forms.CharField(widget=forms.Select(choices=LEVEL_CHOICES))


class AddStockForm(forms.Form):
    level = forms.CharField(widget=forms.Select(choices=LEVEL_CHOICES))
    fabric_type = forms.CharField(widget=forms.Select(choices=FABRIC_CHOICES))
    glove_type = forms.CharField(widget=forms.Select(choices=GLOVES_CHOICES))
    name = forms.CharField()
    quantity = forms.FloatField()


# solve this issue
class deleteEntryForm(forms.Form):
    entry = StockEntry.objects.all()
    ENTRY_CHOICES = [(i.entry_id, i.entry_id) for i in entry]
    entry_id = forms.CharField(widget=forms.Select(choices=ENTRY_CHOICES))
