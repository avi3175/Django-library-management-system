
from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    book_name = serializers.SerializerMethodField()
    free_book_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    book_image = serializers.SerializerMethodField()
    free_book_image = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            'id', 'user', 'user_name', 
            'book', 'book_name', 'book_image', 
            'free_book', 'free_book_name', 'free_book_image', 
            'quantity', 'price', 'total_price'
        ]

    def get_total_price(self, obj):
        return obj.total_price  

    def get_book_name(self, obj):
        return obj.book.book_name if obj.book else None

    def get_free_book_name(self, obj):
        return obj.free_book.book_name if obj.free_book else None

    def get_user_name(self, obj):
        return obj.user.username  

    def get_book_image(self, obj):
        return obj.book.image if obj.book else None  

    def get_free_book_image(self, obj):
        return obj.free_book.image if obj.free_book else None  
