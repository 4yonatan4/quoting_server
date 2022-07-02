from django.urls import path
from . import views

urlpatterns = [
    path('get_bid/', views.get_bid)
]