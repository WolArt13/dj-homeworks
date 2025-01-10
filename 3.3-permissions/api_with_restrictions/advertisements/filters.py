from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    
    created_at = filters.DateFromToRangeFilter()  # Фильтр по дате создания
    creator = filters.NumberFilter(field_name="creator__id")
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)  # Фильтр по статусу

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']  # Поля, по которым будет работать фильтрация
