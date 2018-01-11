from django.contrib import admin

# Register your models here.
from dashboard.models import Processes, Hosts


class HostsAdmin(admin.ModelAdmin):
    model = Hosts
    list_display = ("server_uuid", "ip_addresses", "createtime", "serial_number")


class ProcessesAdmin(admin.ModelAdmin):
    model = Processes
    list_display = ("p_name", "listen_ip_port")


admin.site.register(Processes, ProcessesAdmin)
admin.site.register(Hosts, HostsAdmin)
