# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-24 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20161024_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='host_info',
            name='disk',
            field=models.CharField(blank=True, max_length=10, verbose_name='\u786c\u76d8'),
        ),
        migrations.AddField(
            model_name='host_info',
            name='group',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u6240\u5c5e\u7ec4'),
        ),
        migrations.AddField(
            model_name='host_info',
            name='notes',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AddField(
            model_name='host_info',
            name='owner',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='host_info',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='host_info',
            name='salt_status',
            field=models.BooleanField(default=False, verbose_name='Salt\u72b6\u6001'),
        ),
    ]