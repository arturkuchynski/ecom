from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import *
from parler.admin import TranslatableAdmin, TranslatableStackedInline


class BookImageInline(StackedInline):
    model = BookImage
    max_num = 1
    # set limit for extra entries
    extra = 0


@admin.register(Genre)
class GenreAdmin(TranslatableAdmin):
    # set up fields ordering
    list_display = ['title', 'slug']
    # set up admin search fields
    search_fields = ['title', 'description']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


@admin.register(Book)
class BookAdmin(TranslatableAdmin):
    list_display = ['title', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    inlines = [BookImageInline]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ('book', 'created', 'updated',)
    list_filter = ('book',)

    class Meta:
        model = BookImage

