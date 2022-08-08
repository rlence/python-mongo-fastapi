from fastapi import FastAPI

from server.src.app.user.router import router as router_user
from server.src.app.store.router import router as router_store
from server.src.app.admin.router import router as admin_router

from .db.mongo import client

app = FastAPI()

app.include_router(router_user)
app.include_router(router_store)
app.include_router(admin_router)
