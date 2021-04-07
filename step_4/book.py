from author import Author


class Book:
    def __init__(self, title, revision, authors):
        self.title = title
        self.revision = revision
        self.authors = authors

    def lend(self, userName):
        print(f"Book {self.title} lent by {userName}")
        print(f"Authors: {self.authors.first_name}")