from django.db import models

class FreeBook(models.Model):
    genre = models.ForeignKey("books.Genre", on_delete=models.CASCADE, related_name='free_books')
    image = models.CharField(max_length=2500)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    pages = models.IntegerField()
    trending = models.BooleanField(default=False)
    editor_choice = models.BooleanField(default=False)
    popular_classic = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name
