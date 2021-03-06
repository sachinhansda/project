# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-02 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200430_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_teacher', to='accounts.TeacherProfile'),
        ),
    ]
