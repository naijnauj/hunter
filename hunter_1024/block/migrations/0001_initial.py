# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='版块名称', max_length=100)),
                ('desc', models.CharField(verbose_name='版块描述', max_length=100)),
                ('manager_name', models.CharField(verbose_name='版块管理员名称', max_length=100)),
            ],
        ),
    ]
