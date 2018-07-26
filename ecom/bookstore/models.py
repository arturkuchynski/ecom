from django.db import models
from django.urls import reverse
from isbn_field import ISBNField
from django.core.validators import MinValueValidator
from parler.models import TranslatableModel, TranslatedFields


class Genre(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200,
                               db_index=True),
        slug=models.SlugField(max_length=200,
                              db_index=True,
                              unique=True,
                              help_text='Unique value for book page URL, created from name.'),
        description=models.TextField(blank=True, db_index=True),

    )

    class Meta:
        db_table = 'genres'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookstore:book_list_by_genre',
                       args=[self.slug])


class Book(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200,
                               db_index=True),
        slug=models.SlugField(max_length=200,
                              db_index=True,
                              unique=True),
        author=models.CharField(max_length=100,
                                db_index=True,
                                blank=True,
                                null=True,
                                default=None),
        edition_language=models.CharField(max_length=100,
                                          db_index=True,
                                          blank=True,
                                          null=True,
                                          default=None),
        description=models.TextField(blank=True,
                                     db_index=True),
        binding=models.CharField(max_length=100,
                                 db_index=True,
                                 blank=True,
                                 null=True,
                                 default=None),
    )

    genres = models.ManyToManyField(Genre,
                                    default=None,
                                    blank=True)
    isbn = ISBNField(unique=True,
                     blank=True,
                     null=True,
                     help_text='ISBN is a ten or thirteen digit number used to '
                               'identify books and book-like resources.')

    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    old_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0, max_length=4)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    publisher = models.CharField(max_length=100, blank=True, null=True, default=None)
    pub_year = models.CharField(max_length=4, blank=True, null=True, default=None)
    bestseller = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.discount == 0 and self.old_price >= self.price:
            self.price = self.old_price

        if self.discount != 0:
            self.old_price = self.price
            # calculate discount
            self.price = self.price * (100 - self.discount) / 100

        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bookstore:book_detail',
                       args=[self.id, self.slug])


# FIXME: type object has no attribute '_parler_meta'
class BookImage(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='img/books/%Y/%m/%d', blank=True, null=True, default=None, unique=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'images'
        verbose_name = 'Book Image'
        verbose_name_plural = 'Book Images'
