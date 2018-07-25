from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import logout
from django.urls import path, include
from ecom import settings
from . import views


urlpatterns = [
    path('info/', views.info, name="info"),
    path('login/', views.user_login, name="user_login"),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="user_logout"),
    path('logout/', views.user_logout, name="user_logout"),
    path('change-password/', views.change_password, name="change_password"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('register/', views.user_register, name="user_register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + staticfiles_urlpatterns()