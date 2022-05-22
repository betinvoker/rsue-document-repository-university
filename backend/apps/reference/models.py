from enum import unique
from pyexpat import model
from unicodedata import name
from django.db import models
from django.utils.translation import gettext_lazy as _


class Year(models.Model):
    name = models.PositiveIntegerField(_("Наименование"), unique=True)

    class Meta:
        verbose_name = _("Год защиты ВКР")
        verbose_name_plural = _("Годы защиты ВКР")

    def __str__(self):
        return str(self.name)

class LevelEducation(models.Model):
    name = models.CharField(_("Наименование"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Уровень образования")
        verbose_name_plural = _("Уровни образования")

    def __str__(self):
        return self.name

class Qualification(models.Model):
    code = models.CharField(_("Код"), max_length=25, unique=True)
    name = models.CharField(_("Наименование"), max_length=500)

    class Meta:
        verbose_name = _("Квалификация образования")
        verbose_name_plural = _("Квалификации образования")

    def __str__(self):
        return self.name
