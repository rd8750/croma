# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-15 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_master', '0002_auto_20180822_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='gst_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
