from Commands import *
class Controller:
    def __init__(self,tv):
        self.serial_num= "AB123"
        self.tv= tv
        self.commands=[switch_on_off(self.tv),show_sources(self.tv),switch_signal(self.tv),switch_TVChannel(self.tv)]
        self.current_command = -1

    def show_command(self):
        command_num=1
        for command in self.commands:
            print(str(command_num)+": " + command.__repr__())
            command_num+=1

    def select_command(self):
        while(self.current_command < 1 or self.current_command > 4):
            self.current_command=int(input("select a command: "))

    def execute_command(self):
        self.commands[self.current_command-1].execute()
        self.current_command =-1
