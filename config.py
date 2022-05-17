import os


class Config:
    '''
    General configuration parent class

    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:run@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = 'postgres://zgjbwgpqyaetpj:f87addae0237f9ca08fdbf3da618f4e971ce0d9bb99a74a07c3aef4193f6b349@ec2-44-195-169-163.compute-1.amazonaws.com:5432/d8da1bo60058v'
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
