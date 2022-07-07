from flask import Flask, render_template
from testing import *

app = Flask(__name__)


@app.route('/')
def hello():
    print('test print')
    return foo()