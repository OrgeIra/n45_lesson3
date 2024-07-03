from django.urls import path
from .views import index, books

urlpatterns = [
    path('', index, name='index'),
    path('books/', books, name='books'),
]
