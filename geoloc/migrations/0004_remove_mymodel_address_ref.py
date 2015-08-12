# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0003_mymodel_address_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='address_ref',
        ),
    ]
