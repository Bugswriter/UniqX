from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "04beccaf060f0a03ebfc301930fc1c30"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form Submitting successful")
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form = form )


if __name__=='__main__':
    app.run(debug=True)
