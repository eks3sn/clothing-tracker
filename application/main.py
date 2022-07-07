from flask import Flask, render_template
from testing import *

app = Flask(__name__)


@app.route('/') 
def hello():
    item = Clothing(1, "tank top")
    return item.type