from django_filters import rest_framework as django_filters

from core import models


class Observation(django_filters.FilterSet):

    class Meta:
        model = models.Observation
        fields = ('status', 'approved', 'erroneous')
