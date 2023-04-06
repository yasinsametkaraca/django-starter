from django.urls import path, include
from .views import book_list, book_detail

urlpatterns = [
    path("list/", book_list),
    path("detail/<int:pk>", book_detail)
]
