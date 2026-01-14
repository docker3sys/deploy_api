import os

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", "jsd3HUHD878hs")
ALGORITHM = "HS256"
