from django.urls import path
from .views import FreeBookListCreateView, FreeBookDetailView

urlpatterns = [
    path('free-books/', FreeBookListCreateView.as_view(), name='free-books-list'),
    path('free-books/<int:pk>/', FreeBookDetailView.as_view(), name='free-books-detail'),
]
