from authx import AuthX, AuthXConfig

from src.config import SETTINGS

config = AuthXConfig()
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = SETTINGS.SECRET_KEY
config.JWT_TOKEN_LOCATION = ["headers"]

AUTH = AuthX(config=config)
