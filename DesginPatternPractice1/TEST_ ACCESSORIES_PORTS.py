from unittest import TestCase
from DVD import DVD
from XBOX import XBOX
from HDMI import HDMI
from VGA import VGA


class AccessoryTest(TestCase):
    def test_create_Accessory(self):
        # Arrange
        accessory_description = 'XBOX'
        accessory_port = "HDMI"

        # Act
        accessory = XBOX()
        accessory = HDMI(accessory)
        print(accessory.get_accessory_description(), ", Port: ", accessory.port())
        #
        # Assert
        self.assertEquals(accessory.get_accessory_description(), accessory_description)
        self.assertAlmostEqual(accessory.port(),accessory_port)

    def test_create_Accessory2(self):
        # Arrange
        accessory_description = 'DVD'
        accessory_port = "VGA"

        # Act
        accessory = DVD()
        accessory = VGA(accessory)
        print(accessory.get_accessory_description(), ", Port: ", accessory.port())
        #
        # Assert
        self.assertEquals(accessory.get_accessory_description(), accessory_description)
        self.assertAlmostEqual(accessory.port(), accessory_port)