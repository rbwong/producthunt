# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150331_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='logo',
        ),
        migrations.AddField(
            model_name='country',
            name='logo_url',
            field=models.CharField(default='asd', max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
