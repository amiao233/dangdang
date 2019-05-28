from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from userapp.models import TClass, TUser2, TBook


def booklist(request):
    class1 = TClass.objects.all().values()
    class2 = TUser2.objects.all().values()
    id1 = request.GET.get('id1')
    id2 = request.GET.get('id2')
    num = request.GET.get('num')
    if num == None or num == 'None':
        num =1
    user = request.session.get('user')
    book = TBook.objects.filter(class2_id=id2)
    pagtor = Paginator(book, per_page=4)
    page = pagtor.page(num)
    return render(request, 'booklist.html', {'dad': class1, 'son': class2, 'id1': id1, 'id2': id2, 'page': page, 'user': user})


def book_details(request):
    id = request.GET.get('id')
    user = request.session.get('user')
    if user:
        status = '1'
    else:
        status = '0'
    book = TBook.objects.filter(book_id=id)[0]
    print(book)
    request.session['html'] = 'book_details'
    request.session['book_id'] = id
    return render(request, 'Book details.html', {'book': book, 'user': user, 'status': status, 'id': id})







