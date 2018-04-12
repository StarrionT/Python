from Port_Decorator import PortDecorator


class VGA(PortDecorator):
    def __init__(self, accessory):
        self.accessory = accessory
        self.source = "VGA"

    def get_accessory_description(self):
        return self.accessory.get_accessory_description()

    def port(self):
        return self.source