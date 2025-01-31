from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'free_book', 'quantity', 'price', 'total_price_display')
    list_filter = ('user', 'book', 'free_book')
    search_fields = ('user__username', 'book__book_name', 'free_book__book_name')

    def total_price_display(self, obj):
        return obj.total_price  # Display calculated total price in admin panel
    total_price_display.short_description = "Total Price"

admin.site.register(Cart, CartAdmin)
