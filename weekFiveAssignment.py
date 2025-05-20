# Parent class: Book
class Book:
    def __init__(self, title, author, pages):
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages

    # Method to display book info
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    # Method to simulate reading
    def read(self):
        print(f"You start reading '{self.title}' by {self.author}.")


# Child class: ComicBook (inherits from Book)
class ComicBook(Book):
    def __init__(self, title, author, pages, illustrator):
        # Inherit from parent using super()
        super().__init__(title, author, pages)
        self.illustrator = illustrator  # New attribute for ComicBook

    # Override the display_info method to include illustrator
    def display_info(self):
        super().display_info()
        print(f"Illustrator: {self.illustrator}")

    # New method
    def read_comic(self):
        print(f"You enjoy the colorful art while reading '{self.title}'!")


# Creating objects
normal_book = Book("To Kill a Mockingbird", "Kiwi", 281)
comic = ComicBook("Spider-Man", "Ian Nganga", 50, "Ian Muthoka")

# Using methods
print("📖 Normal Book Info:")
normal_book.display_info()
normal_book.read()

print("\n🦸 Comic Book Info:")
comic.display_info()
comic.read()        # Inherited method
comic.read_comic()  # Unique method
