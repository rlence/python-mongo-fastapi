from typing import Optional
from pydantic import BaseModel
import bcrypt

from server.src.db.mongo import db

user_model = db.get_collection("user")

class User(BaseModel):
    _id: Optional[str | None]
    email: str 
    password: str


    def hash_pass(self):
        hash_pas = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt(14))
        self.password = hash_pas

    def compare_pass(self, password: str):
        return bcrypt.checkpw(password.encode(), self.password.encode())