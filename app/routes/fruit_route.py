from flask import Blueprint
from app.controllers import fruit_constroller, region_table, fruit_table
from app.models.fruit_model import Fruit

Fruit.create_table('region', region_table)
Fruit.create_table('fruit', fruit_table)

bp = Blueprint('fruits', __name__, url_prefix='/fruits')

bp.get('')(fruit_constroller.get_all_fruit)
bp.get('/<int:id>')(fruit_constroller.get_fruit_by_id)
bp.post('')(fruit_constroller.post_fruit)
bp.put('<int:id>')(fruit_constroller.put_fruit)
bp.delete('<int:id>')(fruit_constroller.delete_fruit)
