from django.db import models
from django.contrib.auth import get_user_model
from free_books.models import FreeBook
from books.models import Book

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    free_book = models.ForeignKey(FreeBook, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'book'], name='unique_user_book'),
            models.UniqueConstraint(fields=['user', 'free_book'], name='unique_user_free_book'),
        ]

    def save(self, *args, **kwargs):
        """ Set the price for books (not for free books) """
        if self.book:
            self.price = self.book.price 
        else:
            self.price = 0  
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        """ Calculate total price based on quantity """
        return self.quantity * (self.price or 0)

    def __str__(self):
        return f"{self.user.username} - {self.book or self.free_book} - {self.quantity} - Total: ${self.total_price}"
