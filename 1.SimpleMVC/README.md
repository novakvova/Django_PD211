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
py manage.py runserver 9589
```



