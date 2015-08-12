# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0002_auto_20150812_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='address_ref',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
