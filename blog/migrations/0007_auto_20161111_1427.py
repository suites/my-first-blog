# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161111_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to='uploaded_files/', null=True),
        ),
    ]
