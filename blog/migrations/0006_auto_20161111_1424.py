# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161110_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploaded_files/%Y/%m/%d'),
        ),
    ]
