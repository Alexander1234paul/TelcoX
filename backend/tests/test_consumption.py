from app import create_app
from app.infrastructure.database import db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def setup_module(module):
    global app, client
    app = create_app(TestConfig)  # 🔹 Aquí aplicamos la config de prueba
    with app.app_context():
        db.create_all()
    client = app.test_client()


def teardown_module(module):
    with app.app_context():
        db.drop_all()


def test_get_consumption():
    response = client.get("/api/v1/consumption/1")
    assert response.status_code in [200, 404]
