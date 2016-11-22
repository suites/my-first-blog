# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161111_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('location', models.CharField(max_length=100)),
                ('meeting_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MemberOfMeeting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('member_id', models.IntegerField()),
                ('amount_yn', models.BooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='NumberOfMeeting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('meeting_number', models.CharField(max_length=20)),
                ('total', models.IntegerField(default=0)),
                ('deposit_member_id', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('meeting_id', models.ForeignKey(related_name='number_meeting', to='blog.Meeting')),
            ],
        ),
        migrations.AddField(
            model_name='memberofmeeting',
            name='meeting_number_id',
            field=models.ForeignKey(related_name='member_meeting', to='blog.NumberOfMeeting'),
        ),
    ]
