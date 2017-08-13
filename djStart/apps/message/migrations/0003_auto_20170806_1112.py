# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20170806_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('administrator', '管理员'), ('expert', '专家')], default='expert', max_length=15, verbose_name='用户类型'),
        ),
    ]