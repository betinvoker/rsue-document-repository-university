import django_filters
from .models import PackageDocuments 


class PackageDocumentsFilter(django_filters.FilterSet):
    """
    Фильтр пакетов документов
    """

    class Meta:
        model = PackageDocuments
        fields = [
            "year__name", 
            "level_education__name", 
            "qualification__name", 
            "qualification__code", 
            "teacher_full_name", 
            "students_full_name"
        ]