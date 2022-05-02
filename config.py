class Config(object):
    DEBUG = False

class ProductiionConfig(Config):
    DEBUG = False
class DevelopmentConfig(Config):
    DEBUG = True
    
