from app.infrastructure.database import db


class Account(db.Model):
    __tablename__ = "tbl_accounts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("tbl_users.id"), nullable=False)
    balance = db.Column(db.Float, default=20.0)
    plan_name = db.Column(db.String(50), default="Plan TelcoX Base")
    renewal_date = db.Column(db.Date, default=db.func.current_date())

    user = db.relationship("User", back_populates="account")
