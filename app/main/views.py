from flask import render_template,request,redirect,url_for,abort
from .import main
from flask_login import login_required
from ..models import User
#views
@main.route('/')
def index():
    '''Index method to display the main index page
    '''
    name = "PitchOut"
    title = "PitchOut"
    

    return render_template('index.html' , name = name , title = title )


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)