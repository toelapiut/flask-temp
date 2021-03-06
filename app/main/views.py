from flask import render_template,request,redirect,url_for,abort
from . import main
##remember to import classes from ..requests
from .forms import ReviewForm,UpdateProfile
from .. import db,photos
'''
We then define our route decorators using the 
main blueprint instance instead of the app instance
'''
@main.route('/')
def index():
    
    '''
    View root page function that returns the index
     page and its data
    '''
    message='Hello World Welcome to flask'

    return render_template('index.html', message=message)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form=UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)


@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def  update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photos' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_pic_path=path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

