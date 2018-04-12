from unittest import TestCase
from Cashier import Cashier


class TestCashier(TestCase):
    test = Cashier()
    foods=["The Original BBQ Chicken Chopped","Chinese Chicken"]
    print(test.calculate_price(foods))
    print(test.give_out_change(foods,40))
    print(test.balance)