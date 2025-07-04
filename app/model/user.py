from enum import Enum
from typing import List, Optional
from sqlalchemy.orm import relationship, mapped_column, Mapped, DeclarativeBase
from sqlalchemy import String, ForeignKey, Integer, DateTime, Text, DATE, TIME
from uuid import UUID

class Base(DeclarativeBase):
    pass

class UserRole(Enum):
    ADMIN = "ADMIN"
    EMPLOYEE = "EMPLOYEE"
    SUPER_ADMIN = "SUPER_ADMIN"

class User(Base):
    __tablename__ = "users"
    user_id = mapped_column(UUID, primary_key=True)
    full_name = mapped_column(Text, nullable=False)
    phone_number = mapped_column(Integer, nullable=False)
    email = mapped_column(String(100), nullable=False, unique=True)
    role = mapped_column(UserRole, default=UserRole.EMPLOYEE)
    created_at = mapped_column(DateTime, default=DateTime.now())
    updated_at = mapped_column(DateTime, default=DateTime.now())
