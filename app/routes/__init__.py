from flask import Blueprint, Flask

from .fruit_route import bp as bp_fruit
from .region_route import bp as bp_region
from app.controllers import region_table, fruit_table
from app.models.fruit_model import Fruit

Fruit.create_table('region', region_table)
Fruit.create_table('fruit', fruit_table)

bp_api = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp_api.register_blueprint(bp_fruit)
    bp_api.register_blueprint(bp_region)

    app.register_blueprint(bp_api)