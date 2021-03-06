# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-26 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_no', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.TAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TAPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_no', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.TAProfile')),
            ],
        ),
    ]
