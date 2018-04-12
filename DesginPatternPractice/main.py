from Restaurant import Restaurant


def main():
    CPK = Restaurant()
    for food in CPK.give_menu().keys():
        print(food)
    while CPK.next_custom:

        CPK.take_order()
        print("Your order:")
        for order in CPK.show_order():
            print(order)
        CPK.check()
        print("Your food:")
        for food in CPK.deliver_food():
            print(food)
        print("is READY")

        validation = input("next customer?(Y/N)")
        if validation == 'Y':
            CPK.next_custom = True
        else:
            CPK.next_custom = False


if __name__ == "__main__":
    main()
