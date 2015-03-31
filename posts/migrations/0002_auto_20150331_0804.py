# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='day',
            field=models.CharField(default=-2024, max_length=10, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='discussion_url',
            field=models.URLField(default='http://reddit.com', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='asd', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='redirect_url',
            field=models.URLField(default='http://reddit.com', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tagline',
            field=models.CharField(default='asd', max_length=140, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='votes_count',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
