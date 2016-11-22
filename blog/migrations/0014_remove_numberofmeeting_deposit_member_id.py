# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20161118_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberofmeeting',
            name='deposit_member_id',
        ),
    ]
