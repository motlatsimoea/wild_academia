import django_filters
from .models import Profile



class ProfileFilter(django_filters.FilterSet):

    model = Profile
    fields = ['country', 'district', 'township']