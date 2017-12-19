# pimp_django
https://github.com/talenhao/ProcessInformationManagementPlatform的dashboard
Use sb admin 2 模板 

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

 * run /usr/local/_python3.6.1/bin/uwsgi --ini /home/pimp/uwsgi.ini
