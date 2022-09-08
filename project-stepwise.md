# Project Stepwise

<br>

## Setting up environment

creating virtual environment and installing dependencies.

```powershell
$ mkdir .venv
$ pipenv install
$ pipenv shell
$ pipenv install django
```

creating the django project in the current directory:

```powershell
$ django-admin startproject todo_drf .
```

check if its working by running the dev server.

```powershell
$ python manage.py runserver
```