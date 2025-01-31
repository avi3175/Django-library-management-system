from rest_framework import serializers
from .models import Book, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()  # Returns genre name instead of ID

    class Meta:
        model = Book
        fields = '__all__'
