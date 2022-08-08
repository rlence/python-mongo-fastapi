from server.src.models.user import User
from server.src.app.user import repo
from .model import LogginUser

from server.src.responses.execption import Conflict, NotFound

async def create_user(user: User):
    user_exist = await repo.finde_user_by_email(user.email)
    if user_exist:
        raise Conflict("This email is exist")
    return await repo.create_user(user)

async def user_login(loggin_user: LogginUser):
    user_db = await repo.finde_user_by_email(loggin_user.email)
    if user_db is None:
        raise NotFound("User not found")
    user_db['password'].decode()
    user = User(**user_db)
    pass_is_valid = user.compare_pass(loggin_user.password)
    if pass_is_valid:
        return user
    raise Conflict("The user or pass is not correct")