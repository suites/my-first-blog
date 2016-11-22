# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.CharField(max_length=200),
        ),
    ]
