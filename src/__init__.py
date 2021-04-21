from flask import Flask

app = Flask(__name__, template_folder='views')

from src.controllers import *
from src.routes import *

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

def start_app():
    app.run(port = 3000, debug=True)