from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base, metadata

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, index=True),
    Column('surname', String, index=True),
    Column('email', String, unique=True, index=True),
    Column('password', String),
)

products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('title', String, index=True),
    Column('description', String),
    Column('price', Float),
)

orders = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('prod_id', Integer, ForeignKey('products.id')),
    Column('status', String),
    Column('date', DateTime),
)
