from django_filters import rest_framework as filters
from django_filters.filters import CharFilter
from .models import Post

def get_client_ip(request):
    x_forwarded_for  = request.Meta.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class PostFilter(filters.FilterSet):
    tag = CharFilterInFilter(field_name='tag__name', lookup_expr='in')

    class Meta:
        model = Post
        fields = ['tag']