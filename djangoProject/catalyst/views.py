from django.http import HttpResponse
from django.http import JsonResponse



def index(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return JsonResponse(data)


def detail(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    gender = request.GET.get('gender')

    user = {
        'id': id,
        'name': name,
        'gender': gender
    }

    return JsonResponse(user)