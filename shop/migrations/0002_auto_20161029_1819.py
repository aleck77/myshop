# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': '\u0442\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b'},
        ),
    ]
