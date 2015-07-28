from flask import render_template, flash, redirect, url_for, session, request, g
from postr import app, db
from .forms import RegistrationForm, LoginForm
from .models import User

# Define home page view
@app.route('/')
def home():
	return 'Hello world'

# Define user registration view
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)

	if request.method == 'POST' and form.validate():
		user = User(form.username.data, form.email.data, form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thank you for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

# Define login page view
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)

	if request.method == 'POST':
		if form.validate() == False:
			flash('Invalid credentials')
			return redirect(url_for('login'))
		else:
			session['logged_in'] = True
			return redirect(url_for('home'))

	return render_template('login.html', form=form)

# Define logout page view
@app.route('/logout', methods=['GET', 'POST'])
def logout():
	session['logged_in'] = False
	session.clear()
	return 'Logout page'

# Define User profile page view
@app.route('/user/<user_id>')
def user(user_id):
	return 'User profile'

# Define board page view
@app.route('/boards/<board_id>', methods=['GET', 'POST'])
def boards(board_id):
	return 'This is the board view'