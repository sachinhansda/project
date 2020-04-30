# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-28 06:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_declaration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ta_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]