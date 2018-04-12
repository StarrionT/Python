from Controller import Controller
from Television import Television
from unittest import TestCase

class Test_Controller(TestCase):
    tv= Television()
    controller=Controller(tv)
    controller.show_command()
    controller.select_command()
    controller.execute_command()