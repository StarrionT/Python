from unittest import TestCase
from Menu import *


class TestMenu(TestCase):
    print(get_ingredient("Chinese Chicken"))
    print(get_category("Chinese Chicken"))
    print(get_price('Chinese Chicken'))

    print(get_ingredient("Chicken Piccata"))
    print(get_category("Chicken Piccata"))
    print(get_price('Chicken Piccata'))