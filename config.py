import os
from dotenv import load_dotenv

basedir=os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'n6b)!zl3^+4p(5sfvr2y'
    MAIL_PORT=int(os.environ.get('MAIL_PORT') or 25)
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'microblog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # Email configuration
    EMAIL_USE_SMTP=True
    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL=os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    ADMINS=['chipomwitu88@gmail.com']

    # Pagination
    POSTS_PER_PAGE=20

    # Languages
    LANGUAGES=['en', 'es', 'pt']

    # Elasticsearch
    ELASTICSEARCH_URL=os.environ.get('ELASTICSEARCH_URL')

