from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name = 'bookstore'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<slug:genre_slug>/', views.book_list,
         name='book_list_by_genre'),
    path('<int:id>/<slug:slug>/', views.book_detail,
         name='book_detail'),
    path('contacts/', views.book_list, name='contacts'),
    path('delivery/', views.book_list, name='delivery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + staticfiles_urlpatterns()
