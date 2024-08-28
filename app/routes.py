from app import app, db
from app.models import User
from flask_login import login_user, logout_user, login_required
from flask import render_template,flash, redirect, url_for
from app.forms import RegisterForm, LoginForm


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User {form.username.data} has been registerd seccessfully.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')


@app.route('/<username>/profile')
@login_required
def profile(username):
    """Profile page"""
    user = User.query.filter_by(username=username).first_or_404()
    return render_template(
        'profile.html',
        title='Profile',
        user=user)



@app.route('/about-me')
@login_required
def about_me():
    """About me URL"""
    return render_template('about_me.html', title='about me page')

@app.route('/login', methods=['GET', 'POST'])
def login ():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)