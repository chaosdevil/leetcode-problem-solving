class Book:
    def __init__(self, title, author, price) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare books")

        return self.title == other.title and \
            self.author == other.author and \
                self.price == other.price

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.price >= other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.price < other.price

    # def __getattribute__(self, name):
    #     if name == "price":
    #         p = super().__getattribute__("price")
    #         d = super().__getattribute__("_discount")
    #         return p - (p * d)
    #     return super().__getattribute__(name)

    def __setattr__(self, name, value) -> None:
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)

    def __getattribute__(self, name):
        return name + " is not here!"        
    

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)
b5 = Book("Harry Potter", "J.K. Rowling", 49.95)
b6 = Book("La formule de Dieu", "JR Dos Santos", 19.95)


print(b1 == b4)
print(b1 == b2)

# can't compare book to a non-book
# print(b1 == 42)

print(b1 < b2)
print(b4 < b2)

books = [b5, b6, b1, b3, b2, b4]
books.sort()
print([book.title for book in books])

# b1.price = 38.95
# print(b1)

# b2.price = 40.
# print(b2)

print(b1.randomprop)