import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings 

class PackageDocuments(models.Model):
    """
    Модель
    Пакет документов
    """

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

    def files_rename(self):
        """
        Переименовывает файлы по шаблону
        """
        base =  f"{self.year.name}год_{self.level_education.name}_{self.qualification.code}_{self.teacher_full_name}_{self.students_full_name}"
        name_r = base+"_Отзыв." + self.review.name.split(".")[-1]
        name_g = base+"_ВКР." + self.graduation_work.name.split(".")[-1]
        os.rename(self.review.path, os.path.join(settings.PUBLIC_MEDIA_DIR, name_r))
        os.rename(self.graduation_work.path, os.path.join(settings.PUBLIC_MEDIA_DIR, name_g))
        self.review.name = name_r
        self.graduation_work.name = name_g 
        self.save()

    def __str__(self):
        return self.teacher_full_name