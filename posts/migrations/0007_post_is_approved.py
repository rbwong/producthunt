# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20150331_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
