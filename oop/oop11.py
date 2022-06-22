
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def bookinfo(self):
        return f"{self.title} by {self.author}"


b1 = Book("War and Peace", "Leo Tolstoy", 1224, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 345, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1224, 39.95)


print(b1.title)
print(b2.author)

print(b1 == b3)

b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())

print(b1 == b3)