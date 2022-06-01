from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status

from .models import ShoppingCart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class ShoppingCartView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        cart = user.cart
        serializer = CartSerializer(cart)
        return Response

    def put(self, request, pk=None):
        cart = request.user.cart
        try:
            cart_item: CartItem = cart.cart_item.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'message': 'there is no such object'},status=status.HTTP_204_NO_CONTENT)
        quantity = request.data.get('quantity')
        cart_item.quantity = int(quantity)
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    def delete(self, request, pk):
        cart = request.user.cart
        try:
            cart_item: CartItem = cart.cart_item.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'message': 'there is no such object'}, status=status.HTTP_204_NO_CONTENT)
        
        cart_item.delete()
        return Response({'message': 'object was deleted successfully'}, status=status.HTTP_200_OK)


class AddProductInCartView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.POST
        serializer = CartItemSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

