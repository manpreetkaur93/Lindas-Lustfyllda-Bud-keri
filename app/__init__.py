from flask import Flask

app = Flask(__name__)

from app import routes
from app.utils import generate_histograms

# Generera histogram när applikationen startar
generate_histograms()
