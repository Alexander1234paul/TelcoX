from app.infrastructure.database import db


class Consumption(db.Model):
    __tablename__ = "tbl_consumptions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("tbl_users.id"), nullable=False)
    data_balance = db.Column(db.Float, default=5.0)
    voice_balance = db.Column(db.Integer, default=100)
    last_update = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    user = db.relationship("User", back_populates="consumption")
