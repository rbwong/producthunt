# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150331_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='short',
            field=models.CharField(default='PH', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
