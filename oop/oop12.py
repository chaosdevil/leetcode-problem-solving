from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    # price: float = field(default=10.0)
    price: float = field(default_factory=price_func)

    # post __init__ is automatically called
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} costs {self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 1224)
b2 = Book("The Catcher in the Rye", "JD Salinger", 345, 29.95)

# b1 = Book()

print(b1.description)
print(b2.description)

