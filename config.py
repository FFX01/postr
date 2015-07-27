
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'Superdupersecret'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///main.db'

class DevConfig(BaseConfig):
	DEBUG = True


