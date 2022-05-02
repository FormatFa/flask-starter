from flask import Flask
from apps.app1.views import app1
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(app1,url_prefix="/app1")
    return app

if __name__=="__main__"    :
    create_app().run(host='0.0.0.0')