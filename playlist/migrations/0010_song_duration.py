# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0009_song_thumb_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
