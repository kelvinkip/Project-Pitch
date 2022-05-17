import os


class Config:
    '''
    General configuration parent class

    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:run@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY ='FlSkPItchA@*ppL'
    UPLOADED_PHOTOS_DEST = "app/static/photos" 

    #email 
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD  = os.environ.get("MAIL_PASSWORD")
   


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:run@localhost/pitch'
   
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
     uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI=uri
   
    
class DevConfig(Config):
   
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
}
