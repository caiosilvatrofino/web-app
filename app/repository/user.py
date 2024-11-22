from app.database import session, Base, engine
from app.models.user import User
from sqlalchemy import select


class UserRepository:

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session
    """
    Realizar toda comunicação com banco de dados

    """

    def get_user_by_id(self, id: int):
        query = select(User).where(User.id == id) # select * from table user // where id ta tabela user é == id parametro
        result = self.session.execute(query).scalars()
        return result.first()

    
    def update_user_by_id(self, id: int, new_name=None):
        ...


    
    def delete_user_by_id(self, id: int):
        user_to_delete = self.get_user_by_id(id)
        self.session.delete(user_to_delete)
        self.session.commit()


    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
