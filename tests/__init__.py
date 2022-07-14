from tests.fixtures.authors import *
from sampler import *
import unittest

from faker import Faker
fake = Faker()

class BookProxy(ExplicitProxy):
    decorating: Book
    id: incrementor("book")
    isbn: fake.isbn10
    name: lambda: fake.sentence(nb_words=5)
    published_date: date_range(datetime(2021, 1, 1), 360) 

class AuthorProxy(ExplicitProxy):
    decorating: Author
    name: fake.name
    books: BookProxy(random_range(1, 5))

class Test(unittest.TestCase):
    def test(self):
        authors = AuthorProxy(3).generate()
        self.assertEqual(3, len(authors))

        for author in authors:
            self.assertTrue(0 < len(author.books) <= 5)