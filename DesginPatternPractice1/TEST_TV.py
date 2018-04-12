from Television import Television
from unittest import TestCase

class Test_Tv(TestCase):
    def test(self):
        tv=Television()
        print(tv.get_source_list())
        tv.switch_on_off()
        tv.switch_on_off()
        tv.switch_on_off()

        tv.display()
        tv.switch_signal(1)
        tv.display()
        tv.switch_signal(2)
        tv.display()
        tv.switch_TV_Channel(20)
        tv.display()