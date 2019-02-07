from flask import render_template
#views
@main.route('/')
def index():
    '''Index method to display the main index page
    '''
    name = "PitchOut"

    return render_template('index.html' , name = name)