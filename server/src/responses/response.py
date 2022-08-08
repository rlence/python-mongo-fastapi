from functools import wraps
from fastapi import HTTPException
from http import HTTPStatus

from .execption import NotFound, Conflict

 
def exception_manager(func):
    @wraps(func)       
    async def wrapper(*args, **kwargs):              
            try: 
                return await func(*args, **kwargs) 

            except NotFound as error: 
                raise HTTPException(HTTPStatus.NOT_FOUND, str(error))

            except Conflict as error:
                print("ESTOY EN EL MANAGER ******")
                print(error)
                raise HTTPException(HTTPStatus.CONFLICT, str(error))
            
            except Exception as err:
                print(err)
                raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR, str(err))
    return wrapper 