# [DJHero2903/GiantsBeacon](<https://github.com/DJHero2903/GiantsBeacon>)

**A python script to control the Farming Simulator 22 Collectors Edition USB beacon outside of the game.**

## Installation

1. Clone this repository `git clone https://github.com/DJHero2903/GaintsBeacon.git` or [download as zip archive](https://github.com/DJHero2903/GiantsBeacon/archive/refs/heads/main.zip),

2. Install python 3.12.4 or higher ensuring it is added to your system PATH,

3. Open PowerShell and install the required dependencies from pypi using pip with the requirements.txt file.
    - `hidapi` - Used to communitcate with the USB beacon.
    - `Cython` - Dependency for the hidapi module.

```powershell
pip install -r requirements.txt
```

## Usage

### Via the command line

- Run the `main.py` script in PowerShell with the below command, apending any of the below options if you wish.

  ```powershell
  python main.py OPTIONS
  ```

### Via a shortcut (Windows only)

Note: Indefinate duration isn't supported by this method.

1. Create a shortcut with the location set as described to the `no-console.pyw` script,
1. Add `pythonw` before the start of the path to the `no-console.pyw` script,
1. Add your chosen options after the path to the `no-console.pyw` script,
1. Click Next,
1. Name your shortcut and click Finish,
1. Double click your shourtcut to make the beacon flash outside of the game.

- The location box should be in this format.

```txt
pythonw SCRIPT_PATH OPTIONS
```

## Options

- Set how many seconds to turn on the beacon for with the `--duration SECONDS` or `-d SECONDS` flags (Duration of 60 seconds maximum, set to 0 for an infinate duration, defaults to 2 seconds).
- Set the type of flash for the beacon to use with the `--type TYPE` or `-t TYPE` flags (Choices of blink or round, defaults to round).

## Credits

- Thank you to [@Microgenital](<https://github.com/Microgenital>) for creating the giants_beacon.py class, you can find it's source [here](<https://github.com/Microgenital/Giants_Software_USB_Beacon>) (MIT Licenced).

## Licence

[MIT Licence](https://github.com/DJHero2903/GiantsBeacon/blob/main/LICENSE)
