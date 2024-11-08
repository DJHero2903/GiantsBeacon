#!/usr/bin/env python3

# Import the required modules.
from giants_beacon import GiantsBeacon
from time import sleep
from argparse import ArgumentParser, ArgumentTypeError
from signal import signal, SIGINT
from sys import exit


def check_positive(value):
    # Ensure that the given duration is above -1.
    
    try:
        x = int(value)
  
        if x >= 0:
            return x
        else:
            raise ArgumentTypeError(f"{value} is not an integer >= 0.")

    except ValueError:
        raise ArgumentTypeError(f"\"{value}\" is not an integer.")

def signal_handler(signal, frame) -> None:
    # On ctrl+c SIGINT signal, turn off beacon before program exit.

    BEACON.device_state("off")
    exit(0)


def main() -> None:
    # Main function.

    # Detect ctrl+c signal interupt.
    signal(SIGINT, signal_handler)

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
        type=check_positive,
        choices=range(0, 61),
        default=2,
        help="""How many seconds to turn on the beacon for,
         60 seconds maximum, set to 0 for an infinite duration,
          default is 2 seconds.""",
        metavar="DURATION",
    )

    PARSER.add_argument(
        "--type",
        "-t",
        type=str.lower,
        choices=["round", "blink", "off"],
        default="round",
        help="""What type of animation to use for the beacon,
         choices are 'round', 'blink', 'off', default is round.""",
        metavar="TYPE",
    )

    args = PARSER.parse_args()

    # Create a global instance of GiantsBeacon.
    global BEACON
    BEACON = GiantsBeacon()

    # Theses while loops to allow the duration to be longer than 10 seconds
    # or indefinate, as the Beacon turns off after 10 seconds automatically.
    if args.duration == 0:
        # Loop for indefinate duration, refreshing
        # the beacons internal timer every 3 seconds.

        print("Press ctrl+c to turn off the beacon.")
        while True:
            BEACON.device_state(args.type)
            sleep(3)

    else:
        # Loop for a given duration, refreshing
        # the beacons internal timer every 3 seconds.

        print("Press ctrl+c to turn off the beacon early.")

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
