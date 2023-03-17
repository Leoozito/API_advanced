import json
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product

@api_view(["GET"]) # obtendo visu de API e no parenteses definindo os metodos de solicitação permitidos
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"}, status=405) # tratando erro http
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return Response(data)