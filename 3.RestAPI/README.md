py -m venv .venv

.venv\Scripts\activate.bat

pip install django

python.exe -m pip install --upgrade pip

django-admin startproject shopapi

cd shopapi

py manage.py runserver 5091

py manage.py migrate

py manage.py startapp product

python manage.py makemigrations

python manage.py migrate

py manage.py createsuperuser

admin

Qwerty1-

py manage.py runserver 5091

pip install djangorestframework

npm create vite@latest my-react-app -- --template react-ts

pip install django-cors-headers