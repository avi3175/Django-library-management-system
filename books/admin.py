from django.contrib import admin
from .models import Book, Genre

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'genre', 'author','price')  # Fields to display

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
