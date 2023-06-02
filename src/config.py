import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")
    # todo
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test_user:random_password@localhost:5432/flask-test-db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")
    
config = {
    "DEV": DevelopmentConfig,
    "PROD": ProductionConfig
}