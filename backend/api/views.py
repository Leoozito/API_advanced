import json
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"]) # obtendo visu de API e no parenteses definindo os metodos de solicitação permitidos
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    return Response(data)