# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20150331_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_mod',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
