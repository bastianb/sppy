import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from sppy import __version__

app = Flask(__name__)
app.config.update(dict(
    VERSION=__version__
))

# Set the logging
log_file = '{dir}/sppy.log'.format(
    dir=os.environ.get('SPPY_LOGDIR', '.'))

file_handler = RotatingFileHandler(
    log_file, maxBytes=800000, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

if app.debug:
    file_handler.setLevel(logging.DEBUG)

app.logger.addHandler(file_handler)

from sppy.views import index
