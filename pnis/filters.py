from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from functools import reduce

class ORFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search_value = request.query_params.get('search[value]', None)
        if search_value:
            or_queries = []
            for field in view.search_fields:  # Asegúrate de definir search_fields en tu vista
                or_queries.append(Q(**{f"{field}__icontains": search_value}))
            if or_queries:
                queryset = queryset.filter(reduce(lambda a, b: a | b, or_queries))
        return queryset