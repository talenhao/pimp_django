from django.shortcuts import render


from django.shortcuts import get_object_or_404
from .models import Processes
from .models import Hosts

# Create your views here.
from django.db.models import Count

server_uuids = Hosts.objects.values("server_uuid").order_by("server_uuid")
process_all = Processes.objects.all()
server_ip_addresses = Hosts.objects.values('ip_addresses').order_by("ip_addresses")


def dashboard(request):
    """
    跳转index
    :param request:
    :return:
    """
    return render(request,
                  "dashboard/index.html")


def index(request):
    """
    展示首页
    :param request:
    :return:
    """
    server_count = server_uuids.count()
    process_count = process_all.count()
    # top_process = Processes.objects.raw('select p_name,count(1) cnt from processes group by p_name order by cnt desc')
    top_process = Processes.objects.values('p_name').annotate(num_processes=Count(1)).order_by('-num_processes')[:8]
    return render(request,
                  "dashboard/pages/index.html",
                  {"server_count": server_count,
                   "process_count": process_count,
                   "server_ip_addresses": server_ip_addresses,
                   "top_process": top_process})


def tables(request, server_uuid=None):
    """
    显示所有数据。
    :param request:
    :param server_uuid:
    :return:
    """
    all_processes = Processes.objects.all().exclude(p_ppid=2).exclude(p_pid__lte=2)
    if server_uuid:
        # for_server_uuid = get_object_or_404(Con, server_uuid=server_uuid)
        all_processes = Processes.objects.filter(server_uuid=server_uuid).exclude(p_ppid=2).exclude(p_ppid=3).exclude(p_pid__lte=3)[:100]
    return render(request,
                  "dashboard/pages/tables.html",
                  {"all_processes": all_processes,
                   "server_ip_addresses": server_ip_addresses,
                   "server_uuid": server_uuid})


def hosts(request):
    all_hosts = Hosts.objects.all()
    return render(request,
                  "dashboard/pages/hosts/hosts.html",
                  {"all_hosts": all_hosts})
