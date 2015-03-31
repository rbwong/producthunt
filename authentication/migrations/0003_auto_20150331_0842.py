# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_account_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
