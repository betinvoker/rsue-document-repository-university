# Generated by Django 3.2.13 on 2022-05-22 19:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
        ('storage', '0002_auto_20220522_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedocuments',
            name='graduation_work',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])], verbose_name='Файл ВКР'),
        ),
        migrations.AlterField(
            model_name='packagedocuments',
            name='qualification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.qualification', verbose_name='Код и наименование ООП'),
        ),
        migrations.AlterField(
            model_name='packagedocuments',
            name='review',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg'])], verbose_name='Файл отзыва'),
        ),
    ]
