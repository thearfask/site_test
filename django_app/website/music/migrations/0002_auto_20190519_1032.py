# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-19 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='alnum_title',
            new_name='album_title',
        ),
    ]