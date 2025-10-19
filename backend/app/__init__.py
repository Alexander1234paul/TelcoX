from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.infrastructure.database import db
from app.presentation.consumption_controller import consumption_bp
from app.domain import user, account, consumption, bill  # importa los modelos


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:4200"]}})

    db.init_app(app)
    app.register_blueprint(consumption_bp, url_prefix="/api/v1")

    return app
