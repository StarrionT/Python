from Controller import Controller
from Television import Television

def main():
    tv = Television()
    controller = Controller(tv)
    print("Turn off tv to end")
    while tv.power:
        print("\n\n")
        controller.show_command()
        controller.select_command()
        controller.execute_command()
        tv.display()


if __name__=="__main__":
    main()