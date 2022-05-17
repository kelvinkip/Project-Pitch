import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://vzypakasnjxkfw:cd710d5ddeaad232d56320bcbed04e25718917241455ef728eee2d7ff059cb6b@ec2-3-229-11-55.compute-1.amazonaws.com:5432/de6nhikq8edmsc'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get('FlSkPItchA@*ppL')
    UPLOADED_PHOTOS_DEST = "app/static/photos" 

    #email 
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD  = os.environ.get("MAIL_PASSWORD")
   


class ProdConfig(Config):
    """
    This is the class which we will use to set the configurations during production stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties

    """

    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # uri = os.environ.get("DATABASE_URL")  # or other relevant config var
    # if uri.startswith("postgres://"):
    #     uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:just@localhost/beem'
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
     uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI=uri
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
