# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-04 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_items_info_server_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_info',
            name='version_bak',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u5907\u4efd\u7248\u672c'),
        ),
        migrations.AddField(
            model_name='items_info',
            name='version_new',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u66f4\u65b0\u7248\u672c'),
        ),
        migrations.AddField(
            model_name='items_info',
            name='version_run',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u7248\u672c'),
        ),
    ]