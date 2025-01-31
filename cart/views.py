from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Cart
from free_books.models import FreeBook
from books.models import Book
from .serializers import CartSerializer

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        book_id = request.data.get("book_id")
        free_book_id = request.data.get("free_book_id")

        print("Received Data:", request.data)  # Debugging

        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                cart_item, created = Cart.objects.get_or_create(user=user, book=book)
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        elif free_book_id:
            try:
                free_book = FreeBook.objects.get(id=free_book_id)
                cart_item, created = Cart.objects.get_or_create(user=user, free_book=free_book)
            except FreeBook.DoesNotExist:
                return Response({"error": "Free book not found"}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return Response({"message": "Book added to cart"}, status=status.HTTP_200_OK)


class UpdateCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_id = request.data.get("cart_id")
        action = request.data.get("action")  # "increase" or "decrease"

        try:
            cart_item = Cart.objects.get(id=cart_id, user=request.user)
            if action == "increase":
                cart_item.quantity += 1
            elif action == "decrease":
                cart_item.quantity -= 1
                if cart_item.quantity == 0:
                    cart_item.delete()
                    return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
            cart_item.save()
            return Response({"message": "Cart updated"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)






class ViewCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

