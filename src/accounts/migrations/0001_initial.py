# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 06:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('alias_name', models.CharField(blank=True, max_length=30, null=True)),
                ('OpeningBalance', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=12, null=True)),
                ('ItNo', models.CharField(blank=True, max_length=30, null=True)),
                ('StNo', models.CharField(blank=True, max_length=30, null=True)),
                ('Type', models.CharField(blank=True, max_length=5, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('Current_Balance', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=12, null=True)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('use_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headname', models.CharField(max_length=150, unique=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('show', models.CharField(blank=True, max_length=5, null=True)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('use_date', models.DateField(blank=True, null=True)),
                ('use_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('address3', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('state', models.CharField(blank=True, max_length=80, null=True)),
                ('country', models.CharField(blank=True, max_length=80, null=True)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('phone1', models.CharField(blank=True, max_length=12, null=True)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('phone3', models.CharField(blank=True, max_length=12, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('dl_no1', models.CharField(blank=True, max_length=30, null=True)),
                ('dl_no2', models.CharField(blank=True, max_length=30, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('lst', models.CharField(blank=True, max_length=50, null=True)),
                ('cst', models.CharField(blank=True, max_length=50, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=50, null=True)),
                ('tin_no', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='YearEnding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('year_pur_id', models.IntegerField(blank=True, null=True)),
                ('year_sale_id', models.IntegerField(blank=True, null=True)),
                ('from_dt', models.DateField()),
                ('to_dt', models.DateField()),
                ('registration_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Registration')),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='head_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Head'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
