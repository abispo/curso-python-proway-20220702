from sqlalchemy.orm import relationship

from database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float


class User(Base):

    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)


class UserProfile(Base):

    __tablename__ = "tb_users_profiles"

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    birth_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="profile", uselist=False)


class Product(Base):

    __tablename__ = "tb_products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)


class Order(Base):

    __tablename__ = "tb_orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("tb_users.id"))
    order_date = Column(DateTime, nullable=False)
    description = Column(String(200), nullable=True)


class OrderDetail(Base):

    __tablename__ = "tb_orders_details"

    product_id = Column(Integer, ForeignKey("tb_products.id"), primary_key=True)
    order_id = Column(Integer, ForeignKey("tb_orders.id"), primary_key=True)
    quantity = Column(Integer, nullable=False, default=1)
    description = Column(String(200), nullable=True)
