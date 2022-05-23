from django.contrib import admin
from .models import PackageDocuments

@admin.register(PackageDocuments)
class PackageDocumentsAdmin(admin.ModelAdmin):
    """
    Регистрация пакета документов в админке
    """
    list_display = ("students_full_name","teacher_full_name","year","level_education","qualification")
    list_filter = ("year","level_education")
    search_fields = ("teacher_full_name","students_full_name")