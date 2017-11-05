# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_block_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='版块名称')),
                ('content', models.CharField(max_length=10000, verbose_name='版块描述')),
                ('status', models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (-1, '删除')])),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_timestamp', models.DateTimeField(verbose_name='最后更新时间', auto_now=True)),
                ('block', models.ForeignKey(verbose_name='版块ID', to='block.Block')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章2',
            },
        ),
    ]
