# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161111_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofmeeting',
            name='deposit_member_id',
            field=models.ForeignKey(to='blog.Member', related_name='deposit_member'),
        ),
    ]
