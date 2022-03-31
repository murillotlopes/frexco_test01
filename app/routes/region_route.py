from flask import Blueprint
from app.controllers import region_controller

bp = Blueprint('region', __name__, url_prefix='/region')

bp.get('')(region_controller.get_all_region)
bp.get('/<int:id>')(region_controller.get_region_by_id)
bp.put('/<int:id>')(region_controller.update_region)
bp.post('')(region_controller.post_region)
bp.delete('/<int:id>')(region_controller.delete_region)
