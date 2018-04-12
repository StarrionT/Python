from Menu_item import *


class PizzaMaker:
    def __init__(self,food_name):
        self.food= Pizza(food_name)

    def PrepareDough(self):
        print("making dough")
    def add_sauce(self):
        print("adding sauce")
    def add_topping(self):
        for ingredient in self.food.ingredients:
            print("add {}".format(ingredient))
    def bake(self):
        print("baking")

    def make_food(self):
        self.PrepareDough()
        self.add_sauce()
        self.add_topping()
        self.bake()

class SaladMaker:
    def __init__(self,food_name):
        self.food= Salad(food_name)

    def cut_veg(self):
        print("cutting veggies")

    def mix_sauce(self):
        print("saucing")

    def add_ingredient(self):
        for ingredient in self.food.ingredients:
            print("add {}".format(ingredient))
    def mix_salad(self):
        print("mixing salad")

    def make_food(self):
        self.cut_veg()
        self.add_ingredient()
        self.mix_sauce()
        self.mix_salad()


class PastasMaker:
    def __init__(self,food_name):
        self.food= Pastas(food_name)

    def boil_noodle(self):
        print("boiling noodle")

    def add_ingredient(self):
        for ingredient in self.food.ingredients:
            print("add {}".format(ingredient))

    def make_sauce(self):
        print("making sauce")

    def mix(self):
        print('mixing all')

    def make_food(self):
        self.boil_noodle()
        self.make_sauce()
        self.add_ingredient()
        self.mix()