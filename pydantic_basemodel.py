from pydantic_util.util import User


user = User(name="Wasi", age=25, email='wasili.aebi@b-nova.com', filepath='./test.txt', is_active=False, is_admin=False)

print(user.dict())



