from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Genre, Book
from cart.forms import CartAddProductForm
from .recommender import Recommender
from cart.cart import Cart


@csrf_protect
def book_list(request, genre_slug=None):
    cart = Cart(request)
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available=True)
    if genre_slug:
        language = request.LANGUAGE_CODE
        genre = get_object_or_404(Genre,
                                  translations__language_code=language,
                                  translations__slug=genre_slug)
        books = genre.book_set.filter(available=True)
    return render(request,
                  'shop/book/list.html',
                  locals())

@csrf_protect
def book_detail(request, id, slug):
    cart = Cart(request)
    language = request.LANGUAGE_CODE
    book = get_object_or_404(Book,
                             id=id,
                             translations__language_code=language,
                             translations__slug=slug,
                             available=True)

    genres = Genre.objects.filter(book=book)

    cart_add_form = CartAddProductForm()
    r = Recommender()
    recommended_books = r.suggest_books_for([book], 4)

    return render(request,
                  'shop/book/detail.html',
                  locals())

@csrf_protect
def contacts(request):
    cart = Cart(request)
    return render(request,
                  'contacts.html',
                  locals())

@csrf_protect
def delivery(request):
    cart = Cart(request)
    return render(request,
                  'delivery.html',
                  locals())