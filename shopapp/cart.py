from userapp.models import TBook


class CartItem:
    def __init__(self, book, amount):
        self.book = book
        self.amount = amount
        self.status = 1


class Cart:
    def __init__(self):
        self.save_price = 0
        self.total_price = 0
        self.cart_item = []

    def sums(self):
        self.total_price = 0
        self.save_price = 0
        for i in self.cart_item:
            if i.status:
                self.total_price += i.book.dprice * i.amount
                self.save_price += (i.book.price - i.book.dprice) * i.amount

    def add_book_toCart(self, bookid):
        for i in self.cart_item:
            if i.book.book_id == int(bookid):
                i.amount += 1
            self.sums()
        book = TBook.objects.filter(book_id=bookid)[0]
        self.cart_item.append(CartItem(book, 1))
        self.sums()

    def modify_cart(self, bookid, amount):
        for i in self.cart_item:
            if i.book.book_id == int(bookid):
                i.amount = amount
        self.sums()

    # def delete_book(self, bookid):
    #     for i in self.cart_item:
    #         if i.book.book_id == int(bookid):
    #             self.cart_item.remove(i)
    #     self.sums()