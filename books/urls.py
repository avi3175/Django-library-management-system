from django.urls import path
from .views import GenreListView, BooksByGenreView, BookDetailView

urlpatterns = [
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/<int:genre_id>/books/', BooksByGenreView.as_view(), name='books-by-genre'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
]
