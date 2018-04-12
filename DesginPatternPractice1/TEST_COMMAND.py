from Television import Television
from unittest import TestCase
from Commands import *


class CommandTest(TestCase):
    def test(self):
        TV = Television()
        TV.display()
        command=switch_on_off(TV)
        command.execute()
        TV.display()
        command = switch_on_off(TV)
        command.execute()
        TV.display()
        command = switch_on_off(TV)
        command.execute()
        TV.display()

        command = show_sources(TV)
        command.execute()
        command = switch_signal(TV)
        command.execute()

        command = switch_TVChannel
        command.execute()

