from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import get_object_or_404
from .models import Processes
from .models import Hosts

# Create your views here.
from django.db.models import Count
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections
from .forms import SearchForm
from django.views.generic import View


server_uuids = Hosts.objects.values("server_uuid").order_by("server_uuid")
server_ip_addresses = Hosts.objects.values('ip_addresses').order_by("ip_addresses")
exclude_list = r"(agetty|mcelog|NetworkManager|polkitd|smartd|lvmetad|dbus-daemon|udevd|auditd|irqbalance|hald-runner" \
               r"|acpid|login|mingetty|qmgr|crond|master|atd|abrtd|console-kit-daemon|hald|automount)+"
process_all = Processes.objects.filter(old_mark=0).exclude(p_ppid=2).exclude(
    p_name__regex=exclude_list).exclude(p_pid__lte=3)


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
    top_process = Processes.objects.filter(old_mark=0).exclude(p_ppid=2).exclude(p_ppid=3).exclude(
        p_pid__lte=3).exclude(p_name__regex=exclude_list).values('p_name').annotate(
        num_processes=Count(1)).order_by('-num_processes')[:8]
    the_oldest_process = process_all.order_by('p_create_time')[0]
    the_newest_process = process_all.order_by('-p_create_time')[0]
    the_latest_update_time = process_all.order_by('-createtime')[0].createtime
    return render(request,
                  "dashboard/pages/index.html",
                  {"server_count": server_count,
                   "process_count": process_count,
                   "server_ip_addresses": server_ip_addresses,
                   "top_process": top_process,
                   "the_oldest_process": the_oldest_process,
                   "the_newest_process": the_newest_process,
                   "the_latest_update_time": the_latest_update_time})


def tables(request, server_uuid=None):
    """
    显示所有数据。
    :param request:
    :param server_uuid:
    :return:
    """
    all_processes = process_all[:100]
    if server_uuid:
        # for_server_uuid = get_object_or_404(Con, server_uuid=server_uuid)
        all_processes = process_all.filter(server_uuid=server_uuid).order_by("p_cmdline").distinct()
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


def search(request):
    ctx = {}
    if 'cmdline' in request.GET:
        connections.create_connection(hosts="127.0.0.1")
        cmdline_query = request.GET["cmdline"]
        if cmdline_query:
            es_search = Search(index="esprocesses").query("match", p_cmdline=cmdline_query)
        else:
            es_search = Search(index="esprocesses")
        result = es_search.scan()
        count = es_search.count()
        ctx["cmdline"] = result
        ctx["count"] = count
        return render(request, "dashboard/pages/search.html", ctx)
