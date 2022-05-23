from django.contrib import admin
from .models import Year, LevelEducation, Qualification


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    """
    Регистрация годов защиты ВКР в админке
    """
    pass


@admin.register(LevelEducation)
class LevelEducationAdmin(admin.ModelAdmin):
    """
    Регистрация уровней образования в админке
    """
    pass


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    """
    Регистрация квалификаций в админке
    """
    pass
