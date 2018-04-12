class switch_on_off:
    def __init__(self,tv):
        self.tv=tv

    def __repr__(self):
        return "Switch Power"

    def execute(self):
        self.tv.switch_on_off()


class show_sources:
    def __init__(self, tv):
        self.tv = tv

    def __repr__(self):
        return "Show Source"

    def execute(self):
        num=0
        for source in self.tv.get_source_list():
            print(str(num)+" " + source)
            num += 1


class switch_signal:
    def __init__(self, tv):
        self.tv = tv

    def __repr__(self):
        return "switch_signal"

    def execute(self):
        signal_num = input("Enter a source number")
        self.tv.switch_signal(int(signal_num))


class switch_TVChannel:
    def __init__(self, tv):
        self.tv = tv

    def __repr__(self):
        return "switch_channel"

    def execute(self):
        channel_num=input("Enter a channel number")
        self.tv.switch_TV_Channel(int(channel_num))

