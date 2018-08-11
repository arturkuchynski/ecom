from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from bookstore.models import Book
from .cart import Cart
from .forms import CartAddProductForm
from promos.forms import PromoCodeApplyForm
from bookstore.recommender import Recommender


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    if cart:
        return redirect('cart:cart_detail')
    return redirect('bookstore:book_list')


# TODO: pass book quantity to form
@login_required(login_url='users:user_login')
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        # for p in Product.objects.filter(translations__title==item['book']):
        #     if str(p)==str(item['book']):.
        #     r = Product.objects.translated(name=item['book'])
        #     print(t)

        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    promo_code_apply_form = PromoCodeApplyForm()

    r = Recommender()
    if cart:
        cart_books = [item['book'] for item in cart]
        recommended_books = r.suggest_books_for(cart_books,
                                                max_results=3)

        return render(request,
                      'cart/detail.html',
                      {'cart': cart,
                       'promo_code_apply_form': promo_code_apply_form,
                       'recommended_books': recommended_books})

    return render(request,
                  'cart/detail.html', locals())
