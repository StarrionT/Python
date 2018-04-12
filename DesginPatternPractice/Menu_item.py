from Menu import *

class Pizza:
    def __init__(self, name):
        self.name = name
        self.ingredients = get_ingredient(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Salad:
    def __init__(self, name):
        self.name = name
        self.ingredients = get_ingredient(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Pastas:
    def __init__(self, name):
        self.name = name
        self.ingredients = get_ingredient(name)

    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name

