import os


class Config:
    SECRET_KEY = 'sakal;sjdal;sdjakl;d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    START_NGROK = os.environ.get('START_NGROK') is not None
