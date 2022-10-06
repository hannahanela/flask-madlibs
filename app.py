from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

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
    """Render homepage"""

    return render_template("selection.html", stories=stories)

    # original solution, saved for comparison
    # prompts = silly_story.prompts
    # return render_template("questions.html", prompts = prompts)


@app.get('/prompts')
def display_prompts():
    """Display prompts for user input"""

    story = request.args.get(f"story")
    prompts = stories[story].prompts

    return render_template("questions.html", story=story, prompts=prompts)


@app.get('/results/<story>')
def create_story(story):
    """Create MadLib from user input"""

    prompts = stories[story].prompts

    ans = {}

    for prompt in prompts:
        ans[prompt] = request.args.get(f"{prompt}")

    result = stories[story].generate(ans)

    return render_template("story.html", result=result)
