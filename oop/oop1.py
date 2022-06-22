class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is secret"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price
    
    def setdiscount(self, amount):
        self._discount = amount


class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book("War and Peace", "Gilderoy Lockheart", 465, 32.50)
b2 = Book("Harry Potter", "JK Rowling", 1104, 46.50)

print(b1.getprice())

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

print(b2._Book__secret)

n1 = Newspaper("New York Times")
print(type(b1) == type(n1))
