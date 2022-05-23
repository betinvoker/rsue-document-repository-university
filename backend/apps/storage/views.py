from django import forms
from django.shortcuts import render
from .models import PackageDocuments
from .forms import PackageDocumentsForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class UploadPackageDocuments(View):

    def get(self, request):
        form = PackageDocumentsForm()

        return render(request, template_name='upload-package-documents.html', context={"form":form})

    def post(self, request):
        form = PackageDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            package_documents_instance = form.save()
            package_documents_instance.files_rename()
            return render(request, template_name='upload-package-documents.html', context={"form":form})
        return render(request, template_name='upload-package-documents.html', context={"form":form})


@method_decorator(login_required, name='dispatch')
class ListPackageDocuments(View):

    def get_list_package_documents(self):
        return PackageDocuments.objects.all()

    def get(self, request):
        form = PackageDocumentsForm()
        objects = self.get_list_package_documents()
        return render(request, template_name='list-package-documents.html', context={"form":form,"objects":objects})

    def post(self, request):
        form = PackageDocumentsForm(request.POST, request.FILES)
        # if form.is_valid():
        #     package_documents_instance = form.save()
        #     package_documents_instance.files_rename()
        #     return render(request, template_name='list-package-documents.html', context={"form":form,"objects":objects})
        return render(request, template_name='list-package-documents.html', context={"form":form,"objects":objects})