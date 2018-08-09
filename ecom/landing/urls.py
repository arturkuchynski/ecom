from django.urls import path
from landing import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('subscription-completed/', views.subscribed, name='subscribed'),
]