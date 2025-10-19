import random
from app.infrastructure.repositories.user_repository import UserRepository
from app.infrastructure.database import db


class ConsumptionService:
    @staticmethod
    def get_user_consumption(user_id: int):
        user = UserRepository.get_user_with_relations(user_id)
        if not user:
            return None

        # Simular consumo
        user.consumption.data_balance = max(
            0, user.consumption.data_balance - random.uniform(0, 0.05)
        )
        user.consumption.voice_balance = max(
            0, user.consumption.voice_balance - random.randint(0, 1)
        )
        db.session.commit()

        last_bill = user.bills[-1] if user.bills else None
        return {
            "user": {
                "name": user.full_name,
                "email": user.email,
                "phone": user.phone_number,
            },
            "plan": {
                "name": user.account.plan_name,
                "renewal_date": user.account.renewal_date.isoformat(),
            },
            "balance": round(user.account.balance, 2),
            "consumption": {
                "data_balance": round(user.consumption.data_balance, 2),
                "voice_balance": user.consumption.voice_balance,
                "last_update": user.consumption.last_update.isoformat(),
            },
            "last_bill": {
                "amount": user.bills[-1].amount if user.bills else None,
                "status": user.bills[-1].status if user.bills else None,
            },
        }
