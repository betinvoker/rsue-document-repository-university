import django_filters
from .models import PackageDocuments 


class PackageDocumentsFilter(django_filters.FilterSet):
    """
    Фильтр пакетов документов
    """

    class Meta:
        model = PackageDocuments
        fields = [
            "year", 
            "level_education", 
            "qualification",
            "teacher_full_name", 
            "students_full_name"
        ]