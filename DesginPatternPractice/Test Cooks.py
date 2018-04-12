from unittest import TestCase
from cooks import *


class TestCooks(TestCase):
    p = PizzaMaker("Hawaiian")
    p.make_food()
    print("\n\n")
    s = SaladMaker("Chinese Chicken")
    s.make_food()

    print("\n\n")
    pas = PastasMaker("Chicken Piccata")
    pas.make_food()

