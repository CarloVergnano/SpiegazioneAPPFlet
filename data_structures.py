import operator

from book import Book

b1 = Book("Title 1", "Author 1", 2008, 300)
b2 = Book("Title 2", "Author 2", 1998, 400)

books = [b1, b2]
books.append(Book("Title 3", "Author 3", 2025, 50))

print("List of books")
for book in books:
    print(book)

b4 = Book("Title 1", "Author 1", 1000, 1)

             # BISOGNA DEFINIRE IL METODO __eq_()__ IN Book
if b1 == b4: # OPPURE SI USERA' QUELLO STANDARD DI Object (RIFERIMENTI)
    print("Books are equal")
else:
    print("Books are not equal")

print("Now, the list is sorted and printed again")

# ORDINAMENTO CON operator.attrgetter()

#sorted_books = sorted(books, key= operator.attrgetter("_year"))

# OPPURE, ORDINAMENTO CON LAMBDA (E POI ATTRIBUTO O FUNZIONE CHE DEFINISCE ALGORITMO DI ORDINAMENTO)

                                              #book.function_with_sort_alg()
#sorted_books = sorted(books, key=lambda book: book._pages, reverse=True)

books.append(Book("Title 5", "Author 5", 2008, 100))
books.append(Book("Title 6", "Author 5", 2008, 500))

# OPPURE ANCORA, ORDINAMENTO CON I METODI DUNDER DEFINITI IN Book

sorted_books = sorted(books)

for book in sorted_books:
    print(book)