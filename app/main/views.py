

from flask import render_template,request,redirect,url_for,abort,flash
from . import main 
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile,Pitchform,Commentform,Upvoteform,Downvoteform 
from .. import db,photos


# views to the index pitch page

@main.route('/')
def index():
    '''View root page function that returns the index page and its data'''

    # pitch = Pitch.query.filter_by().first()
    title = 'Home'
    fintechpitch = Pitch.query.filter_by(category = "fintech")
    realestatepitch = Pitch.query.filter_by(category = "realestate")
    businesspitch = Pitch.query.filter_by(category = "business")
    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
    pitches = Pitch.query.all()
    
    return render_template('index.html', title = title,pitches = pitches, fintechpitch = fintechpitch,realestatepitch = realestatepitch,businesspitch = businesspitch,upvotes=upvotes)

# views to home where pitch category and pitches
# @main.route('/home')
# def home():
#     '''View page function that returns the home page and its data'''

#     fintechpitch = Pitch.query.filter_by(category = "fintech")
#     realestatepitch = Pitch.query.filter_by(category = "realestate")
#     businesspitch = Pitch.query.filter_by(category = "business")
#     title = home
#     upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
#     pitches = Pitch.query.all()


#     return render_template('home.html',title = title, fintechpitch = fintechpitch,realestatepitch = realestatepitch,businesspitch = businesspitch,upvotes=upvotes,pitches=pitches )



# user profile 

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



    # update user bio route

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

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# route to enable profile pic upload
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



# route to pitches page
@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = Pitchform()
    user = current_user
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        
        return redirect(url_for('main.index'))
    return render_template('pitch.html',form=form,user=user)

# comment 
@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = Commentform()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data
        # mainuser_id = current_user._get_current_object().id

        new_comment = Comment(description = description, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('main.new_comment', pitch_id= pitch_id))

    # all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    all_comments = Comment.get_comment(pitch_id)

    return render_template('comments.html', form = form, all_comments = all_comments, pitch = pitch )


# upvotes and downvotes
@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    form = Upvoteform()
    pitch = Pitch.query.get(pitch_id)
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    user = current_user
   
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    form = Downvoteform()
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))

 

# added a dynamic route
# @app.route('/movie/<int:movie_id')
# def movie(movie_id):
#     '''____'''
#     return render_template('movie.html',id=movie_id)