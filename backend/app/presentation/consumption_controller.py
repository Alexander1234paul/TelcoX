from flask import Blueprint, jsonify
from app.application.consumption_service import ConsumptionService

consumption_bp = Blueprint("consumption", __name__)


@consumption_bp.route("/consumption/<int:user_id>", methods=["GET"])
def get_consumption(user_id):
    result = ConsumptionService.get_user_consumption(user_id)
    if not result:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(result), 200
