# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-08 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200502_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='TAAllotment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.TAProfile')),
            ],
        ),
    ]
