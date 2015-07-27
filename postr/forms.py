from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=80)])
	email = TextField('Email Address', [validators.Length(min=6, max=100)])
	password = PasswordField('New Password', [
		validators.Length(min=6, max=100),
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords do not match.')
	])
	confirm = PasswordField('Confirm password')
	