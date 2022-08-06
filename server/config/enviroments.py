import os
from .config import SettingsDev, SettingsProd

ENV = os.getenv("ENV", "DEV")

Eviroment = {
    "DEV": SettingsDev,
    "PROD": SettingsProd
}

settings = Eviroment[ENV]
