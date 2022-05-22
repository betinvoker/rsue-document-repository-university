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
            form.save()
            return render(request, template_name='upload-package-documents.html', context={"form":form})
        return render(request, template_name='upload-package-documents.html', context={"form":form})