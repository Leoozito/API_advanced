from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/update', views.product_update_view),
    # path('<int:pk>/delete/', views.product_delete_view),
    path('<int:pk>/', views.product_detail_view)    
]