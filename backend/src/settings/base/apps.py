DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "widget_tweaks",
    "extra_settings",
    "django_filters",
]

PROJECT_APPS = [
    "apps.users",
    "apps.reference",
    "apps.storage",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
