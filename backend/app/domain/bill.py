from app.infrastructure.database import db


class Bill(db.Model):
    __tablename__ = "tbl_bills"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("tbl_users.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    issue_date = db.Column(db.Date, default=db.func.current_date())
    status = db.Column(db.String(20), default="PAID")

    user = db.relationship("User", back_populates="bills")
