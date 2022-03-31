from flask import Blueprint, Flask

from .fruit_route import bp as bp_fruit

bp_api = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp_api.register_blueprint(bp_fruit)

    app.register_blueprint(bp_api)