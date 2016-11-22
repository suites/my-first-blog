# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161114_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofmeeting',
            name='deposit_member_id',
            field=models.ForeignKey(to='blog.Member', related_name='deposit_meeting_member'),
        ),
    ]
