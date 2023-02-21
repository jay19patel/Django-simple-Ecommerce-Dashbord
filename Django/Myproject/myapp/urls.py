from.import views
from django.urls import path


urlpatterns = [
    path('', views.dashbord, name="dashbord"),
    path('customer/<str:id>/', views.customer, name="customer"),
    path('products/', views.products, name="products"),
    path('update_order/<str:id>/', views.update_order, name="update_order"),
    path('delete_order/<str:id>/', views.delete_order, name="delete_order"),
]