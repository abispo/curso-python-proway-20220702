from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship

from database import Base


class User(Base):

    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    profile = relationship("Profile", back_populates="user", uselist=False)
    financial_accounts = relationship("FinancialAccount", back_populates="user")


class UserProfile(Base):

    __tablename__ = "tb_users_profiles"

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    birth_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="profile", uselist=False)


class FinancialAccount(Base):

    __tablename__ = "tb_financial_accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("tb_users.id"), nullable=False)
    name = Column(String(200), nullable=False)
    balance = Column(Float, default=0)

    user = relationship("User", back_populates="financial_accounts", uselist=False)

    debit_transactions = relationship("Transaction", back_populates="debit_account")
    credit_transactions = relationship("Transaction", back_populates="credit_account")


class Transaction(Base):

    __tablename__ = "tb_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    debit_account_id = Column(Integer, ForeignKey("tb_financial_accounts.id"), nullable=False)
    credit_account_id = Column(Integer, ForeignKey("tb_financial_accounts.id"), nullable=False)
    value = Column(Float, nullable=False)

    # campos do tipo timestamp -> Tipo de campo que armazena a data e a hora de uma operação
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    debit_account = relationship(
        "FinancialAccount",
        back_populates="debit_transactions",
        uselist=False,
        foreign_keys=[debit_account_id]

    )
    credit_account = relationship(
        "FinancialAccount",
        back_populates="credit_transactions",
        uselist=False,
        foreign_keys=[credit_account_id]
    )
