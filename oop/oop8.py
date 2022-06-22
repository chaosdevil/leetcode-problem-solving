# magic methods

class Book:
    def __init__(self, title, author, price) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self) -> str:
        return f"title={self.title}, author={self.author}, price={self.price}"

    
b1 = Book("War and Peace", "Leo Toistoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)

print(str(b1))
print(repr(b2))