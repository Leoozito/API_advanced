from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validate_data)
        title = serializer.validate_data.get('title')
        content = serializer.validate_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_create_view = ProductCreateAPIView.as_view()

# Modo de visualização da API 
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()