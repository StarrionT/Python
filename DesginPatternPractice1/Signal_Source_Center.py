class SignalSourceCenter:
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def __init__(self):
        self.accessory_list = ["TV Channal"]

    def connect(self, device):
        self.accessory_list.append(device)
        print(device.get_accessory_description() + "is connected in " + device.port() + " port.")

    def remove(self, device_num):
        if len(self.accessory_list) >= device_num > 0:
            print(self.accessory_list[device_num].get_accessory_description() +
                  " using " + self.accessory_list[device_num].port() + " is removed.")
            del self.accessory_list[device_num]
