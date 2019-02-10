from flask import render_template,request,redirect,url_for,abort
from .import main
from flask_login import login_required
from ..models import User
from .forms import UpdateProfile
from .. import db

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


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)