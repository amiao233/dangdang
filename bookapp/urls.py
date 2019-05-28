from django.urls import path

from bookapp import views

app_name = 'book_app'

urlpatterns = [
    path('booklist/', views.booklist, name='booklist'),
    path('book_details/', views.book_details, name='book_details'),
    ]