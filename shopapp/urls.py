from django.urls import path

from shopapp import views

app_name = 'shop_app'

urlpatterns = [
    path('car/', views.car, name='car'),
    path('indent/', views.indent, name='indent'),
    path('indent_ok/', views.indent_ok, name='indent_ok'),
    path('add_amount/', views.add_amount, name='add_amount'),
    path('add_book/', views.add_book, name='add_book'),

    ]