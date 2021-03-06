from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OuttakeCommand

from commands.shooter.elevatecommand import ElevateCommand
from commands.shooter.deelevatecommand import DeelevateCommand

from commands.shootcommandgroup import ShootCommandGroup

from commands.lights.solidorangecommand import SolidOrangeCommand
from commands.lights.lightsoffcommand import LightsOffCommand
from commands.lights.rgbchangingcommand import RGBChangingCommand
from commands.lights.increasecyclecommand import IncreaseCycleCommand
from commands.lights.decreasecyclecommand import DecreaseCycleCommand

from commands.lights.twelvedaysofchristmaslightscommandgroup import TwelveDaysOfChristmasLightsCommandGroup
from commands.lights.solidbluecommand import SolidBlueCommand
from commands.lights.solidgreencommand import SolidGreenCommand

def init():
    '''
    Declare all controllers, assign axes to logical axes, and trigger
    commands on various button events. Available event types are:
        - whenPressed
        - whileHeld: cancelled when the button is released
        - whenReleased
        - toggleWhenPressed: start on first press, cancel on next
        - cancelWhenPressed: good for commands started with a different button
    '''

    mainController = LogitechDualShock(0)

    logicalaxes.driveX = mainController.LeftX
    logicalaxes.driveY = mainController.LeftY
    logicalaxes.driveRotate = mainController.RightX

    mainController.Back.whenPressed(ResetCommand())

    mainController.A.whileHeld(SolidOrangeCommand())
    mainController.X.toggleWhenPressed(LightsOffCommand())
    mainController.Y.toggleWhenPressed(RGBChangingCommand())
    mainController.B.whileHeld(TwelveDaysOfChristmasLightsCommandGroup())
    mainController.DPadUp.whileHeld(SolidGreenCommand())
    mainController.DPadDown.whileHeld(SolidBlueCommand())
    mainController.DPadLeft.whileHeld(SolidOrangeCommand())

    mainController.LeftTrigger.whileHeld(DeelevateCommand())
    mainController.LeftBumper.whileHeld(ElevateCommand())



    backupController = LogitechDualShock(1)

    backupController.Back.whenPressed(ResetCommand())

    backupController.A.toggleWhenPressed(SolidOrangeCommand())
    backupController.B.toggleWhenPressed(TwelveDaysOfChristmasLightsCommandGroup())
    backupController.X.toggleWhenPressed(LightsOffCommand())
    backupController.Y.toggleWhenPressed(RGBChangingCommand())

    backupController.LeftTrigger.whileHeld(DeelevateCommand())
    backupController.LeftBumper.whileHeld(ElevateCommand())
