# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20150331_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='country',
            name='logo',
            field=models.ImageField(default='asd', upload_to=b''),
            preserve_default=False,
        ),
    ]
