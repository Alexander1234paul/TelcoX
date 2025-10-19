from app.domain.user import User
from sqlalchemy.orm import joinedload


class UserRepository:
    @staticmethod
    def get_user_with_relations(user_id: int):
        """Obtiene un usuario con todas sus relaciones (cuenta, consumo y facturas)"""
        return (
            User.query.options(
                joinedload(User.account),
                joinedload(User.consumption),
                joinedload(User.bills),
            )
            .filter(User.id == user_id)
            .first()
        )
