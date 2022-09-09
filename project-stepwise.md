# Project Stepwise

<br>

## Basic Django project setup

### Setting up environment

creating virtual environment and installing dependencies.

```powershell
$ mkdir .venv
$ pipenv install
$ pipenv shell
$ pipenv install django
```

creating the django project in the current directory, and also applying migrations.

```powershell
$ django-admin startproject todo_drf .
$ python manage.py migrate
```

check if its working by running the dev server.

```powershell
$ python manage.py runserver
```

## Creating the api app

creating a new app using the following command:

```powershell
$ python manage.py startapp api
```

file: todo_drf/settings.py
```python
INSTALLED_APPS = [
    ...

    'api.apps.ApiConfig' # add this line to add the app to the project
]
```

### Setting up api todo model

creating the todo model.

file: api/models.py
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
```

### creating and applying migrations

```powershell
$ python manage.py makemigrations
$ python manage.py migrate
```

### creating urls, and views

setting up the api url routes.

file: todo_drf/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')) # <- add this line
]
```

file: api/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview")
]
```

creating a basic view.

file: api/views.py
```python
from django.http import JsonResponse

def apiOverview(request):
    return JsonResponse("API BASE POINT", safe=False)
```