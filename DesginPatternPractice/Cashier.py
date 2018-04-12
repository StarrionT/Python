from Menu import *


class Cashier:
    def __init__(self):
        self.balance = 1000

    def calculate_price(self, food_list):
        current_total = 0
        if food_list:
            for food in food_list:
                current_total += get_price(food)
        return current_total

    def give_out_change(self, food_list, amount_paid):
        change = amount_paid - self.calculate_price(food_list)
        self.balance += (amount_paid - change)
        return change
