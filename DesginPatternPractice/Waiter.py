from KitchenOrder import *
from Cashier import Cashier
from Menu import *


class Waiter:
    def __init__(self):
        self.Orders = []
        self.cashier = Cashier()

    def get_menu(self):
        return Menu

    def take_order(self, food_name):
        if food_name in Menu:
            self.Orders.append(KitchenOrder(food_name))
        for Order in self.Orders:
            Order.make_food()

    def get_order(self):
        return [x.__str__() for x in self.Orders]

    def check(self):
        return self.cashier.calculate_price([x.food_name for x in self.Orders])

    def changes(self,amount_paid):
        return self.cashier.give_out_change([x.food_name for x in self.Orders], amount_paid)

    def deliver_foods(self):
        foods = [x.food for x in self.Orders]
        self.Orders = []
        return foods
