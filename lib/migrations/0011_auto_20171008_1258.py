# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0010_auto_20171008_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='prestamo',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]