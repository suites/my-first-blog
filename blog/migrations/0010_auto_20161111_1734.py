# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161111_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberofmeeting',
            name='member_id',
            field=models.ForeignKey(to='blog.Member', related_name='member'),
        ),
    ]
