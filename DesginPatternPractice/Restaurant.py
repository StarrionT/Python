from Waiter import *


class Restaurant(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def __init__(self):
        self.waiter=Waiter()
        self.location = "411 Arroyo Parkway"
        self.name = "CPK"
        self.next_custom = 1

    def take_order(self):
        food=input("'food name' or 'Done':\n")
        while food != 'Done':
            self.waiter.take_order(food)
            food = input("'food name' or 'Done'")

    def give_menu(self):
        return self.waiter.get_menu()

    def show_order(self):
        return self.waiter.get_order()

    def check(self):
        price=self.waiter.check()
        print("Price is {}".format(price))
        amount_paid=float(input("You paid $"))
        print("Your change is {}".format(self.waiter.changes(amount_paid)))

    def deliver_food(self):
        return self.waiter.deliver_foods()
