from server.src.models.user import User, user_model

async def create_user(user: User):
    try:
        user.hash_pass()
        user_model.insert_one(user.dict())
        return user
    except Exception as error:
        print('[ERROR Register User]: ', error)
        raise Exception(error)


async def finde_user_by_email(email):
    try:
        return user_model.find_one({"email": email})
    except Exception as error:
        print("[ERROR USER EMAIL]: ", error)
        raise Exception(error)