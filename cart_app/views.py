from rest_framework.views import APIView
from rest_framework.response import Response

from .helpers import get_cart_or_carts_or_error, get_success_response, get_error_response
from .serializers import CartSerializer

from .models import Cart


class CartAPIView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        return get_cart_or_carts_or_error(pk)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return get_success_response('Cart', serializer)

    def patch(self, request, pk):
        try:
            product = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return get_error_response('Cart')

        serializer = CartSerializer(data=request.data, instance=product, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return get_success_response('Cart', serializer)

    def delete(self, request, pk):
        try:
            product = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            get_error_response('product')

        product.delete()

        return Response({'data': {'message': 'Cart was deleted'}})