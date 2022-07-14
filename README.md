# Setup data class
<pre>
from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    id: int
    isbn: str
    name: str
    published_date: datetime

@dataclass
class Author:
    name: str
    books: List[Book]
</pre>

# Create proxy and sampler
<pre>
from sampler import ExplicitProxy, incrementor, date_range, at_least
from faker import Faker
fake = Faker()

class BookProxy(ExplicitProxy):
    decorating: Book
    id: incrementor("book")
    isbn: fake.isbn10
    name: lambda: fake.sentence(nb_words=5)
    published_date: date_range(datetime(2021, 1, 1), 365)

class AuthorProxy(ExplicitProxy):
    decorating: Author
    name: fake.name
    books: BookProxy(at_least(5))
</pre>

# Create 3 samplers
<pre>
authors = AuthorProxy(3).generate()
</pre>