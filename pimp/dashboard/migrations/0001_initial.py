# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('server_uuid', models.CharField(primary_key=True, max_length=36, serialize=False)),
                ('ip_addresses', models.CharField(max_length=255, unique=True)),
                ('cpu_count', models.IntegerField(blank=True, null=True)),
                ('cpu_freq', models.TextField(blank=True, null=True)),
                ('virtual_memory', models.TextField(blank=True, null=True)),
                ('swap_memory', models.TextField(blank=True, null=True)),
                ('createtime', models.DateTimeField(blank=True, null=True, db_column='CreateTime')),
            ],
            options={
                'db_table': 'hosts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=255)),
                ('p_ppid', models.CharField(max_length=5)),
                ('p_pid', models.CharField(max_length=5)),
                ('p_status', models.CharField(max_length=10)),
                ('p_cwd', models.CharField(max_length=255)),
                ('p_exe', models.CharField(max_length=255)),
                ('p_username', models.CharField(max_length=20)),
                ('p_create_time', models.DateTimeField()),
                ('p_cmdline', models.TextField()),
                ('listen_ip_port', models.TextField(blank=True, null=True)),
                ('createtime', models.DateTimeField(blank=True, null=True, db_column='CreateTime')),
            ],
            options={
                'db_table': 'processes',
                'managed': False,
            },
        ),
    ]
