from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer
from .pagination import CustomPagination  # Import from new location




# List all genres
class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer






# List all books of a specific genre
# class BooksByGenreView(ListAPIView):
#     serializer_class = BookSerializer
#     pagination_class = CustomPagination

#     def get_queryset(self):
#         genre_id = self.kwargs['genre_id']
#         return Book.objects.filter(genre_id=genre_id)




from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer
from .pagination import CustomPagination

class BooksByGenreView(ListAPIView):
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = (SearchFilter,)
    search_fields = ('book_name', 'author', 'genre__genre_name')  # You can add more fields for search

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        return Book.objects.filter(genre_id=genre_id)
















    
# Retrieve a single book
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # Ensure this matches the URL field
