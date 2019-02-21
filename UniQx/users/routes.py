from UniQx import db, bcrypt
from flask import render_template, url_for, flash, redirect, Blueprint
from UniQx.users.forms import RegistrationForm, LoginForm
#from UniQx.users.utils import
from UniQx.models import User
from flask_login import login_user, logout_user, login_required

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You are successfully logged in!', category='success')
            return redirect(url_for('about'))
        else:
            flash('Login unsuccessful! Please check username and password', 'danger')

    return render_template('login.html', title='Login', form = form)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are able to login now", category='success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form = form )

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
