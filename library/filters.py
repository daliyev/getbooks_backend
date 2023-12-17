from django_filters import rest_framework as django_filters
from library.models import Book


class SubCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [
            'subcategory'
        ]