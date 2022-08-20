from database import Base

from sqlalchemy import Column, Integer, String


class User(Base):

    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
