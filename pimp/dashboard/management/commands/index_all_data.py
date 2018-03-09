import elasticsearch_dsl
import elasticsearch_dsl.connections

from django.core.management import BaseCommand
from dashboard.models import Processes
from dashboard.models import Hosts

from dashboard.es_docs import EsProcess


class Command(BaseCommand):
    help = "Index all data to Elasticsearch"

    def handle(self, *args, **options):
        elasticsearch_dsl.connections.connections.create_connection(hosts=["127.0.0.1"])
        for process in Processes.objects.filter(old_mark=0):
            host = Hosts.objects.get(server_uuid=process.server_uuid)
            esp = EsProcess(meta={'id': process.pk},
                            id=process.pk,
                            p_name=process.p_name,
                            p_status=process.p_status,
                            p_cwd=process.p_cwd,
                            p_exe=process.p_exe,
                            p_username=process.p_username,
                            p_create_time=process.p_create_time,
                            p_cmdline=process.p_cmdline,
                            listen_ip_port=process.listen_ip_port,
                            server_uuid=host.server_uuid,
                            old_mark=process.old_mark
                            )
            esp.save()
