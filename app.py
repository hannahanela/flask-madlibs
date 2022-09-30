from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisme"

debug = DebugToolbarExtension(app)

# base.hmtl: title & body
# localhost:5000/
# 5 lines/inputs ****maybe some flexibility here??***
# {{ {noun} }} <inputs name='noun'>
# {{ {verb} }}
# <submit button action='/results' method='??'>

# 1. make new template for story selection
# 2. make new route to render story selection
# 3. update '/' to render selection template


@app.get('/')
def index():
    print(silly_story)
    print(excited_story)
    return render_template("selection.html")

    # prompts = silly_story.prompts

    # return render_template("questions.html", prompts = prompts)

@app.get('/prompts')
def display_prompts():

    #prompts = silly_story.prompts
    # prompts = request.args.get(f"story").prompts

    prompts1 = silly_story.prompts
    prompts2 = excited_story.prompts

    story_instance = request.args.get(f"story")

    if story_instance == 'silly_story':
        prompts = prompts1
    if story_instance == 'excited_story':
        prompts = prompts2


    return render_template("questions.html", prompts = prompts)



@app.get('/results')
def create_story():
    """Create MadLib from user input"""

    # create dict from {prompt: input}
    # silly_story.generate(dict)
    # return render_template(story.html, )

    # dictionary keys = <input name="{{prompt}}"
    # dictionary values = value of the input itself


    # prompts = silly_story.prompts


    ans = {}

    for prompt in prompts:
        ans[prompt] = request.args.get(f"{prompt}")

    # noun = request.args["noun"]

    #  = request.args.get()

    story = silly_story.generate(ans)

    return render_template("story.html", story=story)
