import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'n6b)!zl3^+4p(5sfvr2y'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'microblog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # Email configuration
    EMAIL_USE_SMTP=True
    MAIL_SERVER=os.eviron.get('MAIL_SERVER')
    MAIL_PORT=int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL=os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    ADMINS=['marundurecipeapp@gmail.com']
