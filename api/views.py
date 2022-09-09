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


@api_view(['GET'])
def taskDetail(request: Request, pk: str) -> Response:
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request: Request) -> Response:
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request: Request, pk: str) -> Response:
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request: Request, pk: str) -> Response:
    task: Task = Task.objects.get(id=pk)
    task.delete()

    return Response({"msg": "Item successfully deleted!"})