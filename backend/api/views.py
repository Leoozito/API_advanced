import json
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer
from django.http import JsonResponse

@api_view(["POST"]) # obtendo visu de API e no parenteses definindo os metodos de solicitação permitidos
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data= request.data)
    
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
