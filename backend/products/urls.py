from django.urls import re_path, path
from . import views

urlpatterns = [
    path('<int:pk>/', views.product_detail_view)
]