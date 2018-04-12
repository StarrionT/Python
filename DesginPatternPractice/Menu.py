Menu = {"The Original BBQ Chicken Chopped": ('salad', ["Chicken", "Onion"], 10),
        'Chinese Chicken': ('salad', ['Chicken', 'Green Onion'], 20),
        "Roasted Veggie": ('salad', ["LETTUCE", 'cabbage'], 1),
        "Thai Chicken": ("pizza", ["chilli", "curry", "chicken"], 10),
        "Wild Mushroom": ("pizza", ["white mushroom", 'yellow mushroom'], 10),
        "Hawaiian": ("pizza", ["pineapple", "ham"], 10),
        "Chicken Tequila Fettuccine": ("pastas", ["chicken", "tequila"], 15),
        "Jambalaya Fettuccine": ("pastas", ['Fettuccine', 'salt', 'black pepper'], 16),
        "Chicken Piccata": ("pastas", ["piccata", "rotten chicken"], 17)
        }


def get_ingredient(name):
    if name in Menu.keys():
        return Menu[name][1]
    else:
        return list()


def get_price(name):
    if name in Menu.keys():
        return Menu[name][2]
    else:
        return 0


def get_category(name):
    if name in Menu.keys():
        return Menu[name][0]
    else:
        return "N/A"
