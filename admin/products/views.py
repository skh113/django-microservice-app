import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        publish()
        return Response(serializers.data)

    # /api/products
    def create(self, request):
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data)

    # /api/products/<str:id>
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializers = ProductSerializer(instance=product, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:id>
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        random_user = random.choice(users)
        return Response({"id": random_user.id})
