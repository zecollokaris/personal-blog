import os
class Config:
    #Setting Database location
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://karis:Kar!s123@localhost/blog'

    SECRET_KEY = os.environ.get('SECRET KEY')
     
class ProdConfig(Config):
        # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}