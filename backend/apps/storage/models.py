from ssl import create_default_context
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

class PackageDocuments(models.Model):
    year = models.ForeignKey("reference.Year", verbose_name=_("Год"), on_delete=models.CASCADE)
    level_education = models.ForeignKey("reference.LevelEducation", verbose_name=_("Уровни образования"), on_delete=models.CASCADE)
    qualification = models.ForeignKey("reference.Qualification", verbose_name=_("Код и наименование ООП"), on_delete=models.CASCADE)
    teacher_full_name = models.CharField(_("ФИО научного руководителя"), max_length=500)
    students_full_name = models.CharField(_("ФИО обучающегося"), max_length=500)
    review = models.FileField(_("Файл отзыва"), validators=[FileExtensionValidator(['pdf','jpg'])])
    graduation_work = models.FileField(_("Файл ВКР"), validators=[FileExtensionValidator(['pdf','doc','docx'])])
    create_date = models.DateTimeField(_("Дата и время создания"), auto_now_add=True)
    update_date = models.DateTimeField(_("Дата и время последнего обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Пакет документов")
        verbose_name_plural = _("Пакеты документов")

    def __str__(self):
        return self.teacher_full_name