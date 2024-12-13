# This file is used to mark the 'app' directory as a Python package.

# Optionally, you can add some package-level variables or configurations here.
# For example:
__version__ = '1.0.0'
__author__ = 'Ranjini'

# Import any key functions or classes that you want to make available at the package level.
from .monitor import start_monitor
from .ml_model import train_model, predict_traffic
from .response import block_ip
from .dashboard import app
