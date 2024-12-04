py --version

py -m venv .venv

code .

.venv\Scripts\activate.bat
py -m pip install Django
python.exe -m pip install --upgrade pip

cd blog
py manage.py runserver 9589

deactivate

.venv\Scripts\activate.bat
cd blog
py manage.py migrate



