from UniQx import app
from flask import render_template, url_for, flash, redirect
from UniQx.forms import RegistrationForm, LoginForm
from UniQx.models import User


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{ form.username.data } has been successfully logged in', category='success')
        return redirect(url_for('about'))

    return render_template('login.html', title='Login', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account is been created for { form.username.data }', category='success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form = form )
