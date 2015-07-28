from wtforms import Form, BooleanField, TextField, PasswordField, validators
from .models import User

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=80)])
	email = TextField('Email Address', [validators.Length(min=6, max=100)])
	password = PasswordField('New Password', [
		validators.Length(min=6, max=100),
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords do not match.')
	])
	confirm = PasswordField('Confirm password')
	
class LoginForm(Form):
	username = TextField('Username', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])

	def validate(self):
		if not Form.validate(self):
			return False
		user = User.query.filter_by(username=self.username.data).first()
		if user and user.check_password(self.password.data):
			return True
		else:
			self.username.errors.append('Invalid username or password')
			return False