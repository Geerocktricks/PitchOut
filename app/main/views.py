from flask import render_template
from .import main
from flask_login import login_required
#views
@main.route('/')
def index():
    '''Index method to display the main index page
    '''
    name = "PitchOut"
    title = "PitchOut"

    return render_template('index.html' , name = name , title = title)