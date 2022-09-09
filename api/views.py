from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Task
from .serializers import TaskSerializer

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

@api_view(['GET'])
def taskList(request: Request) -> Response:
    tasks: list[Task] = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)