from django.http import JsonResponse

def apiOverview(request):
    return JsonResponse("API BASE POINT", safe=False)
