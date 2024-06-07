from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name: str
    surname: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    user_id: int
    prod_id: int
    status: str


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int
    date: str

    class Config:
        orm_mode = True
