from django.conf.urls import url
from dashboard import views
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^pages/index.html$', views.index, name='page_index'),
    url(r'^pages/tables.html$', views.tables, name='page_tables'),
    url(r'^pages/hosts/hosts.html$', views.hosts, name='page_hosts'),
    url(r'^serveruuid/(?P<server_uuid>[-\w]+)/$', views.tables, name='page_serveruuid_tables'),
    url(r'^pages/search.html$', views.search, name='search'),
]
