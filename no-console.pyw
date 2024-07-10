#!/usr/bin/env python3

# Import the required modules.
from giants_beacon import GiantsBeacon
from time import sleep
from argparse import ArgumentParser, ArgumentTypeError
from sys import exit


def above_zero(value):
    # Ensure that the given duration is above zero.

    try:
        value = int(value)
        if value < 1:
            raise ArgumentTypeError(f"{value} is not higher than zero!")
    except ValueError:
        raise Exception(f"{value} is not an integer!")
    return value


def main() -> None:
    # Main function.

    # Allow control via command line arguments.
    PARSER = ArgumentParser(
        prog="Giants Beacon Control script",
        description="""Make the Giants FS22 collectors edition beacon flash
        with a choice of animation and duration.""",
        epilog="""Credit to Microgenital for the beacon control class.
          (MIT Licenced)""",
    )

    PARSER.add_argument(
        "--duration",
        "-d",
        type=above_zero,
        choices=range(1, 61),
        required=True,
        help="""How many seconds to turn on the beacon for,
         1 to 60 seconds, this option is required.""",
        metavar="DURATION",
    )

    PARSER.add_argument(
        "--type",
        "-t",
        type=str.lower,
        choices=["round", "blink"],
        default="round",
        help="""What type of animation to use for the beacon,
         choices are 'round' or 'blink', default is round.""",
        metavar="TYPE",
    )

    args = PARSER.parse_args()

    # Create a global instance of GiantsBeacon.
    global BEACON
    BEACON = GiantsBeacon()

    # Loop for a given duration, refreshing
    # the beacons internal timer every 3 seconds.

    countdown = args.duration
    while countdown > 0:

        if countdown >= 3:
            BEACON.device_state(args.type)
            sleep(3)
            countdown -= 3

        else:
            BEACON.device_state(args.type)
            sleep(countdown)
            countdown = 0

    BEACON.device_state("off")

    exit(0)


# Only run this code if this file is ran directly,
# not when imported by another program.
if __name__ == "__main__":
    main()
