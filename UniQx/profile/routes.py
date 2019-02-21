from flask import render_template, flash
from UniQx.models import User
from flask_login import login_required


@app.route('/<username>')
@login_required
def account(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('account.html', title='Profile', user = user)
    else:
        flash("There is no account with this username")
        return render_template('404.html')
