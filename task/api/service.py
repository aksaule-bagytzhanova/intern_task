from django_filters import rest_framework as filters
from django_filters.filters import NumberFilter
from .models import Post

def get_client_ip(request):
    x_forwarded_for  = request.Meta.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
class NumberFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class PostFilter(filters.FilterSet):
    tag = NumberFilterInFilter(field_name='tag__id', lookup_expr='in')

    class Meta:
        model = Post
        fields = ['tag']