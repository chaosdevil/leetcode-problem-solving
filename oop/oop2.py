class Book:
    book_types = ("Hardcover", "Paperback", "Ebook")
    __booklist = None

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.book_types:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    def set_title(self, newtitle):
        self.title = newtitle

    # class method
    @classmethod
    def getbooktypes(cls):
        return cls.book_types

    # static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

print("Book types: ", Book.getbooktypes())

b1 = Book("Title 1", "Hardcover")
b2 = Book("Title 2", "Ebook")
b3 = Book("Title 3", "Paperback")

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)