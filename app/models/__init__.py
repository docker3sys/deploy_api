from .base import Base, engine
from .user import User
from .test import Test
from .result import Result

# Создание всех таблиц
Base.metadata.create_all(bind=engine)