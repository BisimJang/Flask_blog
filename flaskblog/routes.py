from flaskblog import app
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.models import User, Post

posts = [{'author': 'Jason Jang',
          'title': 'Aafari',
          'content': 'The Enfant Terrible',
          'date_posted': '22nd Nov, 2024'
          }
    ,
         {'author': 'Z',
          'title': 'Draw, Damn it',
          'content': 'An artistic monologue',
          'date_posted': '13th Nov, 2024'
          }]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
