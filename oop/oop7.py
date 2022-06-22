class Book:
    def __init__(self, title, price, author=None) -> None:
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount

        return result


class Author:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount) -> None:
        self.name = name
        self.pagecount = pagecount

author = Author("Leo", "Toistoy")
b1 = Book("War and Peace", 39.0, author)

b1.add_chapter(Chapter("Chapter 1", 125))
b1.add_chapter(Chapter("Chapter 2", 97))
b1.add_chapter(Chapter("Chapter 3", 102))

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())