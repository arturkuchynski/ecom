from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from cart.cart import Cart
from bookstore.models import Genre
from .forms import SubscribeForm


def landing(request):
    form = SubscribeForm(request.POST or None)

    if request.POST and form.is_valid():

        message = """
        Hello there!

        I wanted to personally write an email in order to welcome you to our platform.
        We have worked day and night to ensure that you get the best service . I hope
        that you will enjoy the the . We send out a newsletter once a
        week. Make sure that you read it. It is usually very informative.

        Cheers!
        @Artur Kuchynski, bookstore admin
            """
        email = request.POST['email']
        send_mail('Welcome!', message, "Artur Kuchynski, bookstore admin",
                  [email], fail_silently=False)
        new_form = form.save()

        return render(request, 'subscribed.html', locals())

    return render(request, 'landing.html', locals())


def subscribed(request):
    return redirect(reverse('bookstore:book_list'))
