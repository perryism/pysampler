from dataclasses import dataclass
from typing import List
from datetime import datetime

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