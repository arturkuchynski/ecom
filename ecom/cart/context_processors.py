from .cart import Cart


def cart(request):
    """
    Pass a cart object when use this context processor
    """
    return {'cart': Cart(request)}
