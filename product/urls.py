from django.urls import path
from product.views import CreateProductsView, ReadProductsView, DelProductsView, ReadAllProductsView, UpdateProductsView, SoftDelProductsView

urlpatterns = [
    path('products/', ReadAllProductsView.as_view(), name="products-read-all"),
    path('products/<int:pk>/', ReadProductsView.as_view(), name="products-read"),
    path('products-create/', CreateProductsView.as_view(), name="products-create"),
    path('products-update/<int:pk>/', UpdateProductsView.as_view(), name="products-update"),
    path('products-soft-del/<int:pk>/', SoftDelProductsView.as_view(), name="products-soft-del"),
    path('products-hard-del/<int:pk>/', DelProductsView.as_view(), name="products-hard-del"),
]