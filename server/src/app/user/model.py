from pydantic import BaseModel

class LogginUser(BaseModel):
    email: str
    password: str