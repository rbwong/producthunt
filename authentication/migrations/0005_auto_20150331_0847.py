# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20150331_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_superuser',
        ),
    ]
