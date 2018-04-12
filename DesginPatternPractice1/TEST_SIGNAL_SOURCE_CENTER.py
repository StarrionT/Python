from unittest import TestCase
from Signal_Source_Center import SignalSourceCenter
from DVD import DVD
from XBOX import XBOX
from HDMI import HDMI
from VGA import VGA

class SignalSourceCenterTest(TestCase):
    def test(self):
        xbox = XBOX()
        xbox = HDMI(xbox)

        dvd = DVD()
        dvd = VGA(dvd)

        ssc = SignalSourceCenter()
        ssc.connect(xbox)
        ssc.connect(dvd)

        ssc.remove(1)
        ssc.remove(6)

