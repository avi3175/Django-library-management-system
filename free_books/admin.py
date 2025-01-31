from django.contrib import admin
from .models import FreeBook

@admin.register(FreeBook)
class FreeBookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'genre', 'author')  
    search_fields = ('book_name', 'author') 
    list_filter = ('genre',) 

