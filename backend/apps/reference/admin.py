from django.contrib import admin
from .models import Year, LevelEducation, Qualification

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    pass

@admin.register(LevelEducation)
class LevelEducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    pass