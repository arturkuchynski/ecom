from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from ecom import settings
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:book_id>/',
         views.cart_add,
         name='cart_add'),
    path('remove/<int:book_id>/',
         views.cart_remove,
         name='cart_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + staticfiles_urlpatterns()
