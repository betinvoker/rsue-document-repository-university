from django.forms import ModelForm
from .models import PackageDocuments


class PackageDocumentsForm(ModelForm):
   """
   Форма загрузки пакетов документов
   """

   class Meta:
      model = PackageDocuments
      fields = ["year", "level_education", "qualification", "teacher_full_name", "students_full_name", "review", "graduation_work"]