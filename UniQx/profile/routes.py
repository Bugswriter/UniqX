from flask import render_template, flash, Blueprint
from UniQx.models import User
from flask_login import login_required, current_user
from UniQx.profile.forms import ProfileForm

profile = Blueprint('profile', __name__)

@profile.route('/<username>/update')
@login_required
def set_profile(username):
    form = ProfileForm()
    user = User.query.filter_by(username=username).first()
    if user == current_user:
        return render_template('create_profile.html', title='Profile', form = form)
    else:
        flash("You are not allowed on this page")
        return render_template('403.html')
