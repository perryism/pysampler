incrementors = {}
def incrementor(name):
    def f(): 
        global incrementors 
        c = incrementors.get(name, 0)
        c += 1
        incrementors[name] = c
        return c 
    return f

from random import randrange
from datetime import datetime, timedelta

def date_range(start_date, days_between_dates):
    def f():
        random_number_of_days = randrange(days_between_dates)
        return start_date + timedelta(days=random_number_of_days)
    return f

import random
def random_range(s, e):
    return lambda : random.randint(s, e)

def at_least(e):
    return random_range(1, e)

from .proxy import Proxy, ExplicitProxy