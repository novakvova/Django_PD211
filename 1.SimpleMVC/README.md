```
py --version
py -m venv .venv
code .
```

```
.venv\Scripts\activate.bat
py -m pip install Django
python.exe -m pip install --upgrade pip
cd blog
py manage.py runserver 9589
deactivate
```

```
.venv\Scripts\activate.bat
cd blog
py manage.py startapp posts
py manage.py migrate
```

```
--------------------
.venv\Scripts\activate.bat
pip install mysqlclient
pip install mariadb
cd blog
python manage.py migrate
```
```
py manage.py runserver 9589
py manage.py makemigrations
python manage.py migrate
```

---------Testing ORM----------
```
py manage.py shell
>>>from posts.models import Post
>>>p=Post()
>>>p
>>>p.title="Пост №1. Краще ви вигулювати собак у парку."
>>>p.save()
>>>Post.objects.all()
>>>exit()
```

```
cd blog
py manage.py shell
>>>from posts.models import Post
>>>p=Post()
>>>p.title="Пост №2. Пошук козачки :)."
>>>p.save()
>>>Post.objects.all()
>>>exit()
```

```
.venv\Scripts\activate.bat
cd blog
py manage.py createsuperuser
admin

AdminKrot1+
py manage.py runserver 9589
```

```
cd blog
pip install Pillow
py manage.py makemigrations
python manage.py migrate
```

Global Database
```
https://filess.io/

roxejep832@ronete.com
KabanKrot!*D-+

Server: miq8f.h.filess.io
Name: django_frameeast
Username: django_frameeast
Password: 906bb29409c08e6449e3576f904e48fb8b502f9c
Port number: 3305
```

-------Add Super user--------
.venv\Scripts\activate.bat
cd myblog
py manage.py migrate
py manage.py createsuperuser
admin

SuperAdminKrot1-
```

