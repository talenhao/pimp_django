# pimp_django
A dashboard for Porcess Information Management Platform (PIMP 进程信息平台)

agent is here:
   https://github.com/talenhao/ProcessInformationManagementPlatform
**Use sb admin 2 template

 * rename pimp/dashboard/templates/dashboard/pages/common/otherlinks.html.for_git to otherlinks.html, you can add your Friendship links in this page.
 * rename pimp/dashboard/templates/dashboard/pages/common/otherlinksinmainpage.html.for_git to otherlinksinmainpage.html, you can add some thing as timeline.
 * change pimp/pimp/settings.py
  * add you server ip in 
```
ALLOWED_HOSTS = ['192.168.1.1', '127.0.0.1']"
```
  * change database infomations
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pimp',
        'USER': 'pimp',
        'PASSWORD': 'pimp',
        'HOST': '192.168.1.1',
    }
}
```
 * pip install uwsgi
 * Add processes from db to elasticsearch.
 * run /usr/local/_python3.6.1/bin/python3 manage.py index_all_data
 * run /usr/local/_python3.6.1/bin/uwsgi --ini /home/pimp/uwsgi.ini


## 页面展示
![image](https://github.com/talenhao/pimp_django/blob/master/imgs/pimp-3.png?raw=true)
![image](https://github.com/talenhao/pimp_django/blob/master/imgs/pimp-2.png?raw=true)
![image](https://github.com/talenhao/pimp_django/blob/master/imgs/pimp-1.png?raw=true)
![image](https://github.com/talenhao/pimp_django/blob/master/imgs/pimp-4.png?raw=true)
![image](https://github.com/talenhao/pimp_django/blob/master/imgs/pimp-5.png?raw=true)
