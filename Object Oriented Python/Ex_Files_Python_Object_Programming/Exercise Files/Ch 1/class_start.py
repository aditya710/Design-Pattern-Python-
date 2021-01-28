# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPE = ("HardCover", "Ebook", "PaperBack")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPE


    # TODO: create a static method
    @staticmethod
    def getbookList():
        if Book.__booklist == None:
            Book.__booklist = []

        return Book.__booklist
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPE):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HardCover")
b2 = Book("Title 2", "PaperBack")

# TODO: Use the static method to access a singleton object
thebooks = Book.getbookList()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
