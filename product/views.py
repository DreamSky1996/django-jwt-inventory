from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from product.models import Product
from product.serializers import ProductSerializer
from product.decorators import validate_request_data
from product.permissions import IsAdmin, IsManage, IsRead

class CreateProductsView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    permission_classes = (permissions.IsAuthenticated, IsManage)
    
    def post(self, request, *args, **kwargs):
        a_product = Product.objects.create(
            data=request.data["data"],
        )
        return Response(
            data=ProductSerializer(a_product).data,
            status=status.HTTP_201_CREATED
        )

class UpdateProductsView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    permission_classes = (permissions.IsAuthenticated, IsManage)
    
    def put(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"], del_flag=False)
            a_product.data = request.data["data"]
            a_product.save()
            return Response({"status": "success"})
        except Product.DoesNotExist:
             return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class SoftDelProductsView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    permission_classes = (permissions.IsAuthenticated, IsManage)
    
    def get(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"], del_flag=False)
            a_product.del_flag = True
            a_product.save()
            return Response({"status": "success"})
        except Product.DoesNotExist:
             return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ReadProductsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    permission_classes = (permissions.IsAuthenticated, IsRead)
    
    def get(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"], del_flag=False)
            return Response(ProductSerializer(a_product).data)
        except Product.DoesNotExist:
             return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ReadAllProductsView(generics.RetrieveAPIView):
    queryset = Product.objects.all().filter(del_flag=False)
    permission_classes = (permissions.IsAuthenticated, IsRead)
    def get(self, request):
        # products = self.queryset.all()
        products = self.queryset.all()
        serializer_class = ProductSerializer(products, many=True)
        return Response(serializer_class.data)
        
class DelProductsView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    permission_classes = (permissions.IsAuthenticated, IsAdmin)

    def delete(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            a_product.delete()
            return Response(data={"status": "success"},status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )