# python-parrot
## Requirements
- Ubuntu or Debian based linux distribution
- Wifi card/adapter
- Python 3.7 or newer recommended
- parrot bebop2 drone or anafi4k
## Setup
- Install olympe shell through the  guide here: https://developer.parrot.com/docs/olympe/
- Download the python script [here](PythonParrot.py)
- Install python keyboard module with `pip3 install keyboard`
- Install python camera  module with `pip3 install opencv-python`(might not use in final product and doesn't do anything too special as of yet)
- The `speed` integer sets the speed for piloting commands in a range of 0 to 100 in the python script
## How to use
- open a terminal window in the folder of the python script or navigate to it
- run `sudo -s` for sudo privileges as the keyboard module needs this
- run `source ~/code/parrot-groundsdk/./products/olympe/linux/env/shell` to initiate the olympe shell
- execute the python script with `python3 PythonParrot.py`
## Controls
- `T` take off
- `L` landing
- `Q` quit
- `P` start piloting mode
  - `8` go forwards
  - `2` go backwards
  - `4` go left
  - `6` go right
  - `7` turn left
  - `9` turn right
  - `1` go down
  - `3` go up
  - `R` toggle recording mode, will make a file called recordedpath.txt in the python scripts folder
  - `L` toggle replay mode
  - `E` exit piloting mode
