import configparser
import sys
import time
import os
import pathlib

import threading

from seedsigner.controller import Controller
from seedsigner.helpers import touchscreen

config = configparser.ConfigParser()

base_path = pathlib.Path(__file__).absolute().parent
config_path = base_path.joinpath("settings.ini")
print(f"Using config file: {config_path}")
config.read(config_path)

print(config.sections())
# Dont load RPi Deps
os.environ["NOTAPI"] = "yes"

# import glob
# print(glob.glob("*"))
# import code
# code.interact(local=locals())

# One-time setup to intialize the one and only Controller
# Controller.configure_instance(config, disable_hardware=True)
Controller.configure_instance(config)

# Get the one and only Controller instance and start our main loop
controller = Controller.get_instance()
x = threading.Thread(target=controller.start)
x.start()
controller.disp.mainloop()
# controller.start()
