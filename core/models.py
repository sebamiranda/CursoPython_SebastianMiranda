from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    recommended_age = models.IntegerField(blank=True, null=True)


class Partner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.IntegerField(max_length=8)
    date_joined = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    book_name = models.CharField(max_length=50, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)


class BookLoan(models.Model):
    status = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_prestamo = models.DateTimeField(auto_now_add=True)
    date_devolucion = models.DateTimeField(auto_now=True)