from elasticsearch_dsl import DocType
from elasticsearch_dsl import Integer
from elasticsearch_dsl import Text
from elasticsearch_dsl import Date


class EsProcess(DocType):
    id = Integer()
    p_name = Text()
    p_status = Text()
    p_cwd = Text()
    p_exe = Text()
    p_username = Text()
    p_create_time = Date()
    p_cmdline = Text()
    listen_ip_port = Text()
    server_uuid = Text()
    old_mark = Integer()

    class Meta:
        doc_type = 'processes'
        index = 'esprocesses'
