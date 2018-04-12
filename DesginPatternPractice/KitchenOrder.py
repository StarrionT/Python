from Menu import *
from cooks import *


def get_maker(food_name):
    if get_category(food_name) == 'salad':
        return SaladMaker(food_name)
    if get_category(food_name) == 'pizza':
        return PizzaMaker(food_name)
    if get_category(food_name) == 'pastas':
        return PastasMaker(food_name)
    else:
        return None


class KitchenOrder:
    def __init__(self, food_name):
        self.food = None
        self.cook = get_maker(food_name)
        self.food_name = food_name

    def make_food(self):
        if self.cook is not None:
            self.cook.make_food()
            self.food = self.cook.food
        else:
            print("error!")

    def __repr__(self):
        return "Order of " + self.cook.food.__str__()

