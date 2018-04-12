from unittest import TestCase
from Menu_item import *


class TestMenuItem(TestCase):
    p = Pizza("Hawaiian")
    print(p.name)
    print(p.ingredients)
