from wpilib.command.command import Command

import subsystems

class ManualUpCommand(Command):

    def __init__(self):
        super().__init__('Manual Up')

        self.requires(subsystems.elevator)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass