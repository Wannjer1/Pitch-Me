
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import InputRequired




class Pitchform(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    description = TextAreaField('Your one minute pitch, starts now!,',validators=[InputRequired()])
    category = RadioField('Label', choices=[('fintech','fintech'),('realestate','realestate'),('business','business')],validators=[InputRequired()])
    submit = SubmitField('Submit')

class Commentform(FlaskForm):
	description = TextAreaField('Add comment',validators=[InputRequired()])
	submit = SubmitField('Submit')

class Upvoteform(FlaskForm):
	submit = SubmitField('Submit')


class Downvoteform(FlaskForm):
	submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')