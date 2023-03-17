import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    print(body) 
    data = {}
    try:
        data = json.loads(body) # Para converter um json para um dicionario em python
    except:
        pass 
    print(data.keys())
    data['headers'] = request.headers # request.META
    data['content_type'] = request.content_type 
    return JsonResponse(data)
