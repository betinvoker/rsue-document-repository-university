# Generated by Django 3.2.13 on 2022-05-22 17:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedocuments',
            name='graduation_work',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Файл ВКР'),
        ),
        migrations.AlterField(
            model_name='packagedocuments',
            name='review',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Файл отзыва'),
        ),
    ]
