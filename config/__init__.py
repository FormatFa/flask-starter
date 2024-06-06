class Config(object):
    debug = False


class ProductiionConfig(Config):
    debug = False
class DevelopmentConfig(Config):
    debug = True
    # 关闭模版缓存配置
    TEMPLATES_AUTO_RELOAD=True
    CACHE_TYPE="null"

config = DevelopmentConfig()
