from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=160, null=False, unique=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal('1.00'), validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_created=True, auto_now=True, null=True)
    last_changed_at = models.DateTimeField(auto_now_add=True, null=True)
    pages = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    authors = models.ManyToManyField('Author', blank=False)
    publisher = models.ForeignKey('Publisher', null=True, default=None, blank=True, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.title} - {self.pages} - {self.price} grn'

    def __len__(self):
        return self.pages if self.pages >= 0 else 0


class Author(models.Model):
    name = models.CharField(max_length=100, default='')
    pseudonym = models.CharField(max_length=100, default='')
    has_bad_temper = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ---'


class AuthorDetails(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()


class Publisher(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.name} **'


class VisitCounter(models.Model):
    visitors = models.IntegerField(default=0)
