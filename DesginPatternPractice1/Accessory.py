import abc


class Accessory(object):
    __metaclass__ = abc.ABCMeta

    description = "Some Accessory"

    def __init__(self, name, port):
        self.name = name
        self.source = source

    def get_accessory_description(self):
        return self.description

    @abc.abstractmethod
    def port(self):
        pass