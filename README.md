# pimp_django
https://github.com/talenhao/ProcessInformationManagementPlatform的dashboard
Use sb admin 2 模板 

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

 * run /usr/local/_python3.6.1/bin/uwsgi --ini /home/pimp/uwsgi.ini
