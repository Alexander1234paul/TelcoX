from app.infrastructure.database import db


class User(db.Model):
    __tablename__ = "tbl_users"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    account = db.relationship("Account", back_populates="user", uselist=False)
    consumption = db.relationship("Consumption", back_populates="user", uselist=False)
    bills = db.relationship("Bill", back_populates="user", cascade="all, delete-orphan")
