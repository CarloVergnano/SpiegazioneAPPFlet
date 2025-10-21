
class Book:
    def __init__(self, title, author, year, pages):
        self._title = title
        self._author = author
        self._year = year
        self._pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def __str__(self):
        return f"{self._title}, {self._author}, {self._year}, {self._pages}"

    def __eq__(self, other):
        # ALGORITMO DI CONFRONTO, PIU' O MENO COMPLESSO
        return self._title == other._title and self._author == other._author # COSI SE UN LIBRO AVRA LO STESSO TITOLO E STESSO AUTORE SARA UGUALE

    def __lt__(self, other):
        # ALGORITMO DI ORDINAMENTO, ES. PER ANNO CRESC., E PER PAGINE DECRESC.
        if self._year == other._year:
            return self._pages > other._pages
        else:
            return self._year < other._year

