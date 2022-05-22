from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from apps.storage.views import UploadPackageDocuments
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("admin/", admin.site.urls,name="admin"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "", UploadPackageDocuments.as_view(), name="package-documents-form"
    ),
]



if settings.DEBUG:

    # pylint: disable=ungrouped-imports
    from django.conf.urls.static import static

    urlpatterns = (
        [
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )