from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=255, unique=True)
    image = models.CharField(max_length=2500)

    def __str__(self):
        return self.genre_name

class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    image = models.CharField(max_length=2500)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    trending = models.BooleanField(default=False)
    editor_choice = models.BooleanField(default=False)
    popular_classic = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name
