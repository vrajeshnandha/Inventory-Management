from .models import Variance
import django_filters


class VarianceFilter(django_filters.FilterSet):
    class Meta:
        model = Variance
        fields = ['date', 'name', 'fabric_name']
