import os


class Config:
    '''
    General configuration parent class

    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:run@localhost/pitch'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vzypakasnjxkfw:cd710d5ddeaad232d56320bcbed04e25718917241455ef728eee2d7ff059cb6b@ec2-3-229-11-55.compute-1.amazonaws.com:5432/de6nhikq8edmsc'
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
   
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

   
    
class DevConfig(Config):
   
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
}
