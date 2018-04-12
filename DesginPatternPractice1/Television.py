from Controller import Controller
from Signal_Source_Center import SignalSourceCenter
from DVD import DVD
from XBOX import XBOX
from HDMI import HDMI
from VGA import VGA


class Television:
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def __init__(self):
        xbox = XBOX()
        dvd = DVD()
        self.xbox = HDMI(xbox)
        self.dvd = VGA(dvd)

        self.SignalSourceCenter = SignalSourceCenter()
        self.SignalSourceCenter.connect(self.xbox)
        self.SignalSourceCenter.connect(self.dvd)
        self.current_source = 0

        self.current_TVChannel = 0
        self.brand = "Sony"
        self.model = "XBR55X850C"

        self.power = True

    def switch_signal(self,device_num):
        self.current_source = device_num
        print("switch to device " + self.get_source_list()[self.current_source])

    def get_source_list(self):
        source_list = ["TV Channel"]

        for device_num in range(1,len(self.SignalSourceCenter.accessory_list)):
            device = self.SignalSourceCenter.accessory_list[device_num]
            source_list.append(device.get_accessory_description() + " using " + device.port())
        return source_list

    def switch_on_off(self):
        self.power = not self.power
        if self.power:
            print("switching on")
        else:
            print("switching off")

    def switch_TV_Channel(self,channel_num):
        if channel_num >= 0:
            self.current_source = 0
            self.current_TVChannel=channel_num
            print("switching to Channel "+ str(channel_num))

    def display(self):
        if self.power:
            if self.current_source:
                device=self.SignalSourceCenter.accessory_list[self.current_source]
                print("displaying " + device.get_accessory_description() + " using " + device.port())
            else:
                print("displaying TV Channel "+ str(self.current_TVChannel))
        else:
            print("I'm off")

