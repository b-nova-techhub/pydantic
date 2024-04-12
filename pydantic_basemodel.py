from pydantic_util.util import User


user = User(name="Wasi", age=25, email='wasili.aebi@b-nova.com', filepath='./test.txt', is_active=False, is_admin=True, )

print(user.dict())




# bought= 0
# filtepath= './test.txt'
# is_active= True
# from util_own_type import User
# bought=2