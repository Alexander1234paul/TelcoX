from app import create_app
from app.infrastructure.database import db
from app.domain.user import User
from app.domain.account import Account
from app.domain.consumption import Consumption
from app.domain.bill import Bill

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if not User.query.first():
            user = User(
                full_name="Alexander Quinatoa",
                email="pquinatoa@gmail.com",
                phone_number="0963117079",
            )
            db.session.add(user)
            db.session.flush()

            account = Account(
                user_id=user.id, balance=20.0, plan_name="Plan TelcoX Base"
            )
            consumption = Consumption(
                user_id=user.id, data_balance=5.0, voice_balance=100
            )
            bill = Bill(user_id=user.id, amount=19.99, status="PAID")

            db.session.add_all([account, consumption, bill])
            db.session.commit()

    app.run(host="0.0.0.0", port=5000, debug=True)
