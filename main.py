from dataclasses import dataclass
from typing import Dict, List
from tkinter import *
from tkinter import filedialog
from os import path
from functools import partial
from colorama import Fore, init
import json

import sys
from PyQt5.QtWidgets import *
import Main_window

app = QApplication(sys.argv)

Application = Main_window.App()
Application.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    print('Closing Window...')

