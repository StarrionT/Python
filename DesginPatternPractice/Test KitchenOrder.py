from unittest import TestCase
from KitchenOrder import KitchenOrder


class TestKitchenOrder(TestCase):
    KO = KitchenOrder("Hawaiian")
    KO.make_food()
    print(type(KO.cook))
    print((KO.food))

    KO = KitchenOrder("Chinese Chicken")
    KO.make_food()
    print(type(KO.cook))
    print((KO.food))

    KO = KitchenOrder("Bob")
    KO.make_food()
    print(type(KO.cook))
    print((KO.food))

    KO = KitchenOrder("Chicken Piccata")
    KO.make_food()
    print(type(KO.cook))
    print((KO.food))

    print(KO)