import abc
from Accessory import Accessory


class PortDecorator(Accessory):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_port_description(self):
        pass
