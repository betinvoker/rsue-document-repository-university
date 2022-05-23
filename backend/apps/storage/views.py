from django import forms
from django.shortcuts import render
from .models import PackageDocuments
from .forms import PackageDocumentsForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import PackageDocumentsFilter
from django.core.paginator import Paginator

@method_decorator(login_required, name='dispatch')
class UploadPackageDocuments(View):
    """
    Обработка страницы загрузки
    пакета документов
    """

    def get(self, request):
        """
        Обработка GET запроса
        """
        form = PackageDocumentsForm()
        return render(request, template_name='upload-package-documents.html', context={"form":form})

    def post(self, request):
        """
        Обработка POST запроса
        """
        form = PackageDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            package_documents_instance = form.save()
            package_documents_instance.files_rename()
            return render(request, template_name='upload-package-documents.html', context={"form":form, "object":package_documents_instance})
        return render(request, template_name='upload-package-documents.html', context={"form":form})


@method_decorator(login_required, name='dispatch')
class ListPackageDocuments(View):
    """
    Обработка страницы списка
    пакетов документов
    """

    COUNT_ELEMENTS_PAGE = 1

    def get_list_package_documents(self):
        """
        Возвращает базовый queryset
        пакета документов
        """
        return PackageDocuments.objects.all()

    def get(self, request):
        """
        Обработка GET запроса
        """
        filter = PackageDocumentsFilter(request.GET, self.get_list_package_documents())
        paginator = Paginator(filter.qs,self.COUNT_ELEMENTS_PAGE)
        return render(request, template_name='list-package-documents.html', context={"form":filter.form,"page_objects":paginator})

