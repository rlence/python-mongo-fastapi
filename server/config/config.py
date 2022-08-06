import os

class Settings:
    mongo_user: str = os.getenv("MONGO_USERNAME")
    mongo_pass: str = os.getenv("MONGO_PASSWORD")

class SettingsDev(Settings):
    mongo_database: str = 'test'
    mongo_host_port: str = 'mongodb'

class SettingsProd(Settings):
    mongo_database: str = os.getenv("MONGO_DATABASE")
    mongo_host_port: str = os.getenv("MONGO_HOST_PORT")
