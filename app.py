from flask import Flask
from apps.app1.views import app1
from config import config
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(app1,url_prefix="/")

    return app

if __name__=="__main__"    :
    create_app().run(host='0.0.0.0',debug=True)