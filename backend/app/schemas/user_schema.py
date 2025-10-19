from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.domain.user import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


user_schema = UserSchema()
