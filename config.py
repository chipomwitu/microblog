import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'n6b)!zl3^+4p(5sfvr2y'
