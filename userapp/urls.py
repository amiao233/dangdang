from django.urls import path

from userapp import views

app_name = 'user_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register_ok/', views.register_ok, name='register_ok'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('check_name/', views.check_name, name='check_name'),
    path('check_pwd/', views.check_pwd, name='check_pwd'),
    path('get_captcha/', views.get_captcha, name='get_captcha'),
    path('check_captcha/', views.check_captcha, name='check_captcha'),
    path('quit/', views.quit, name='quit'),
    ]