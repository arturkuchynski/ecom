from django.urls import path
from . import views

app_name = 'promos'

urlpatterns = [
    path('apply/', views.promo_code_apply, name='apply'),
]
