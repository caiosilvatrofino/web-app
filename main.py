from app.repository.user import UserRepository
from app.models.user import User

user_repo = UserRepository()

user = User()
user.email = 'caiohenrique@gmail.com'
user.address = 'Rua engenheiro pegado 312'
user.password = 'daskdskadsakdnsa'
user.name = 'caiohenrique'

user_repo.create_user(user)


# result = user_repo.get_user_by_id(1)

# print(result.__dict__)

# user_repo.delete_user_by_id(2)

user_repo.update_user_by_id(1, 'josefin')