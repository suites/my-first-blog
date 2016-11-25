# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20161124_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberofmeeting',
            name='meeting_member',
        ),
        migrations.AddField(
            model_name='memberofmeeting',
            name='meeting_number',
            field=models.ForeignKey(to='blog.NumberOfMeeting', null=True, related_name='member_meeting'),
        ),
    ]
