from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisme"

debug = DebugToolbarExtension(app)

# base.hmtl: title & body
# localhost:5000/
# 5 lines/inputs ****maybe some flexibility here??***
# {{ {noun} }} <inputs name='noun'>
# {{ {verb} }}
# <submit button action='/results' method='??'>


@app.get('/')
def index():
    noun = request.args["noun"]
    
    return render_template("questions.html", noun=noun)
