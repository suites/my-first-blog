# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_numberofmeeting_deposit_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='numberofmeeting',
            name='deposit_member',
            field=models.ForeignKey(null=True, to='blog.Member', related_name='deposit_meeting_member'),
        ),
    ]
