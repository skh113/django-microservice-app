from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)

    # /api/products
    def create(self, request):
        pass

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        pass

    # /api/products/<str:id>
    def update(self, request, pk=None):
        pass

    # /api/products/<str:id>
    def destroy(self, request, pk=None):
        pass
