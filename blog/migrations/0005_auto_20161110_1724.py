# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161110_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='rank',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
