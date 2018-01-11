# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Hosts(models.Model):
    server_uuid = models.CharField(primary_key=True, max_length=36)
    ip_addresses = models.CharField(unique=True, max_length=255)
    cpu_count = models.IntegerField(blank=True, null=True)
    cpu_freq = models.TextField(blank=True, null=True)
    virtual_memory = models.TextField(blank=True, null=True)
    swap_memory = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosts'

    def __str__(self):
        return self.server_uuid


class Processes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    p_name = models.CharField(max_length=255)
    p_ppid = models.IntegerField()
    p_pid = models.IntegerField()
    p_status = models.CharField(max_length=10)
    p_cwd = models.CharField(max_length=255)
    p_exe = models.CharField(max_length=255)
    p_username = models.CharField(max_length=20)
    p_create_time = models.DateTimeField()
    p_cmdline = models.TextField()
    listen_ip_port = models.TextField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    server_uuid = models.ForeignKey(Hosts, db_column='server_uuid')

    class Meta:
        managed = False
        db_table = 'processes'

    def __str__(self):
        return self.p_name
