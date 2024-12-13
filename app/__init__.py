# Initialize the 'app' package

# Optionally, define version and author information (metadata)
__version__ = '1.0.0'
__author__ = 'Ranjini'

# Import necessary modules and functions to make them accessible at the package level
from .monitor import start_monitor
from .ml_model import train_model, predict_traffic
from .response import block_ip
from .dashboard import app
