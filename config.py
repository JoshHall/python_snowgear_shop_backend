import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    STRIPE_SECRET_KEY = 'sk_test_hZrdgq5APkXTMmTC1GyL6OJf'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('https://git.heroku.com/snow-gear-shop-backend.git') or 'sqlite:///' + os.path.join(basedir, 'app.db')
