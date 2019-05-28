import hashlib
import os
from userapp.models import TClass, TUser2, TUser, TBook

import re

from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse


from userapp.captcha.image import ImageCaptcha
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from dangdang import settings
from userapp import models

import random, string

def hash_code(name, now):
    """
    谁调此方法就为谁返回一个随机的验证码
    :param name:
    :param now:
    :return:
    """
    h = hashlib.md5()
    name += now
    h.update(name.encode())
    return h.hexdigest()


def make_confirm_string(new_user):
    """
    为用户生成随机验证码并将验证码保存在数据库中
    :param new_user:
    :return:
    """
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = hash_code(new_user.email_addr, now)
    return code


def send_email(email, code):
    subject = 'python157'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/user/user_confirm/?code={}&user={}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1:8080', code, email)
    #发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    # 发送的html文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_confirm(request):
    """
    用户处理用户发起邮箱验证的请求
    :param request: 用户发来的验证码
    :return:
    """
    user_code = request.GET.get('code')
    user = request.GET.get('user')
    confirm = models.Confirm_string.objects.get(code=user_code)
    if confirm:
        # 将用户状态改为可登陆
        request.session['user'] = user
        TUser.objects.filter(user_name=user)[0].status = 1
        # 删除验证码
        return redirect('user_app:register_ok')
    else:
        return HttpResponse('验证失败')


def index(request):
    class1 = TClass.objects.all().values()
    class2 = TUser2.objects.all().values()
    print(class1)
    print(class2)
    user = request.session.get('user')
    books = TBook.objects.filter('books')[0]
    return render(request, 'index.html', {'dad': class1, 'son': class2, 'user': user, 'books': books})


def login(request):
    name1 = request.COOKIES.get('name')
    pwd1 = request.COOKIES.get('pwd')
    if name1 != None:
        if TUser.objects.filter(user_name=name1, user_password=pwd1).count():
            request.session['user'] = name1
            return redirect('user_app:index')
    return render(request, 'login.html')


def login_logic(request):
    name = request.POST.get('txtUsername')
    password = request.POST.get('txtPassword')
    txt_vcode1 = request.POST.get('txt_vcode')
    txt_vcode2 = request.session.get('code')
    user = TUser.objects.filter(user_name=name)
    password = TUser.objects.filter(user_password=password)
    if user:
        if password == password and txt_vcode1 == txt_vcode2:
            request.session['login'] = 'ok'
            request.session['user'] = name
            return redirect('user_app:index')
    else:
        return HttpResponse('h1>请输入正确的密码</h1>'
                '<a href="/user_app/login/">点击跳转回到注册界面！</a>')


def register(request):
    return render(request, 'register.html')


def register_ok(request):
    user_name = request.POST.get('txt_username')
    password1 = request.POST.get('txt_password')
    password2 = request.POST.get('txt_repassword')
    txt_vcode = request.POST.get('txt_vcode')
    txt_vcode1 = request.session.get('code')
    print(122, txt_vcode, txt_vcode1)
    TUser.objects.filter(user_name=user_name, user_password=password1)
    if TUser.objects.filter(user_name=user_name):
        return HttpResponse('该用户已存在')
    else:
        if password1 == password2 and txt_vcode == txt_vcode1:

            return render(request, 'register ok.html')
        else:
            return render(request, 'register.html')


def check_name(request):
    name = request.GET.get('name')
    user = TUser.objects.filter(user_name=name)

    def checkEmail(email):
        result = re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)
        if result is not None:
            return 1
        else:
            return 0
    if user:
        return HttpResponse('1')
    else:
        if checkEmail(name):
            return HttpResponse('2')
        else:
            return HttpResponse('0')


def check_pwd(request):
    pwd = request.GET.get('pwd')
    if (pwd.isdigit or pwd.isalpha) and len(pwd) <= 4:
        return HttpResponse('1')
    elif 8 > len(pwd) > 4 and (pwd.isdigit or pwd.isalpha):
        return HttpResponse('2')
    else:
        return HttpResponse('3')


def get_captcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits, 1)
    random_code ="".join(code)
    request.session['code'] = random_code
    data = image.generate(random_code)
    return HttpResponse(data, "image/png")


def check_captcha(request):
    code1 = request.session.get('code')
    code2 = request.GET.get('code')
    if code1.lower() == code2.lower():
        return HttpResponse('1')
        #验证成功
    else:
        return HttpResponse('0')


def quit(request):
    request.session['login'] = None
    request.session['user'] = None
    request.session['car'] = None
    return HttpResponse('0')