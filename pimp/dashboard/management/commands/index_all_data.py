import elasticsearch_dsl
import elasticsearch_dsl.connections
from django.core.management import BaseCommand
from dashboard import es_docs
from dashboard.views import process_all
from dashboard.models import Hosts
from dashboard.views import es_index_name


class Command(BaseCommand):
    help = "Index all data to Elasticsearch"

    def handle(self, *args, **options):
        index_name = es_index_name
        elasticsearch_dsl.connections.connections.create_connection(hosts=["127.0.0.1"])
        if elasticsearch_dsl.Index(name=index_name).exists():
            elasticsearch_dsl.Index(name=index_name).delete()
        for process in process_all:
            print("Now process %r" % process.pk)
            host = Hosts.objects.get(server_uuid=process.server_uuid)
            esp = es_docs.EsProcess(meta={'id': process.pk},
                                    id=process.pk,
                                    p_name=process.p_name,
                                    p_status=process.p_status,
                                    p_cwd=process.p_cwd,
                                    p_exe=process.p_exe,
                                    p_username=process.p_username,
                                    p_create_time=process.p_create_time,
                                    p_cmdline=process.p_cmdline,
                                    listen_ip_port=process.listen_ip_port,
                                    # server_uuid=host.server_uuid,
                                    server=host.ip_addresses,
                                    old_mark=process.old_mark
                                    )
            esp.save()
