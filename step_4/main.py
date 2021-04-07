import book
import author

first_author = author.Author("John", "Doe", "Australian")
loan_book = book.Book("All about Python", 1, first_author)

loan_book.lend("testUser")