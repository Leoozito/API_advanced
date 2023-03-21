from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_detail_view)
]