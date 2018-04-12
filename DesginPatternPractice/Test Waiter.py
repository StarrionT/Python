from unittest import TestCase
from Waiter import Waiter


class TestWaiter(TestCase):
    w = Waiter()
    print(w.get_menu())
    w.take_order("The Original BBQ Chicken Chopped")
    w.take_order("The Original BBQ Chicken Chopped")
    w.take_order('Chinese Chicken')
    print(w.get_order())
    print("Price is {}".format(w.check()))
    print("Change is {}".format(w.changes(100)))
