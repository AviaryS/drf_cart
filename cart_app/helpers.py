from rest_framework.response import Response

from cart_app.models import Cart
from cart_app.serializers import CartSerializer


def get_success_response(key_name, serializer):
    return Response({f'{key_name}': serializer.data})


def get_error_response(obj_name):
    return Response({'error': {'message': f'{obj_name} not found'}}, status=404)


def get_carts():
    try:
        serializer = CartSerializer(Cart.objects.all(), many=True)
    except Cart.DoesNotExist:
        return get_error_response('Carts')
    return get_success_response('Carts', serializer)


def get_cart_by_id_or_error(pk):
    try:
        serializer = CartSerializer(Cart.objects.get(pk=pk))
    except Cart.DoesNotExist:
        return get_error_response('Cart')
    return get_success_response('Cart', serializer)


def get_cart_or_carts_or_error(pk):
    if not pk:
        return get_carts()
    else:
        return get_cart_by_id_or_error(pk)