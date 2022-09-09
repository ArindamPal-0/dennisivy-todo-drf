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

## Setting up Django REST Framework

### Installing Django REST Framework

```powershell
$ pipenv install djangorestframework
```

### Adding DRF to the project

file: todo_drf/settings.py
```diff
INSTALLED_APPS = [
    ...

    'api.apps.ApiConfig',
+   'rest_framework',
]
```

### Converting the view to return DRF response

file: api/views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

@api_view(['GET'])
def apiOverview(request: Request) -> Response:

    api_urls: dict[str, str] = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'
    }

    return Response(api_urls)
```

you can view the response at the url http://127.0.0.1:8000/api/

## Returning Serialized list of Task Model


### Creating admin user and registering Task Model to the admin page

creating admin user

```powershell
$ python manage.py createsuperuser
```

registering Task model on the admin page


file: api/admin.py
```python
from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
```

### Creating the task-list route

creating `TaskSerializer`

file: api/serializers.py
```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
```

creating the appropriate url and view:

file: api/urls.py
```diff
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
+   path('task-list/', views.taskList, name="task-list")
]
```

file: api/views.py
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def taskList(request: Request) -> Response:
    tasks: list[Task] = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
```