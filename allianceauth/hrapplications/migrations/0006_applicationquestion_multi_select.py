# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapplications', '0005_remove_legacy_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationquestion',
            name='multi_select',
            field=models.BooleanField(default=False),
        ),
    ]
