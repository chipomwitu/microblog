import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

from config import Config

from elasticsearch import Elasticsearch

from flask import Flask, request, current_app
from flask_babel import Babel
from flask_babel import lazy_gettext as _1
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os


login=LoginManager()
login.login_view='auth.login'
login.login_message=_1('Please log in to access this page.')

babel=Babel()
bootstrap=Bootstrap()
db=SQLAlchemy()
mail=Mail()
migrate=Migrate()
moment=Moment()


def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)

    login.init_app(app)
    babel.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    app.elasticsearch=Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    if not app.debug:
        # Send errors to email
        if app.config['MAIL_SERVER']:
            auth=None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure=None
            if app.config['MAIL_USE_TLS']:
                secure=()
            mail_handler=SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Microblog App Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        # Log errors to a file

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler=RotatingFileHandler('logs/microblog.log', maxBytes=10240,
            backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')

    return app

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
    # return 'pt'
    # return 'es'

from app import models

