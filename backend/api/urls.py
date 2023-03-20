from django.urls import re_path, path, include
from  . import views

urlpatterns = [
    path('', views.api_home),
    # path('products/', include('products.urls'))
]