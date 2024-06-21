from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Supplier(Base):
    """
    Supplier model representing a supplier in the database.

    Attributes:
        id (int): Primary key.
        name (str): Supplier name.
    """
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


class Product(Base):
    """
    Product model representing a product in the database.

    Attributes:
        id (int): Primary key.
        code (str): Product code.
        name (str): Product name.
        category (str): Product category.
        price (float): Product price.
        stock (int): Product stock.
        supplier_id (int): Foreign key referencing the supplier.
        update_date (datetime): Date of the last update.
    """
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, unique=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    update_date = Column(DateTime, default=datetime.now)
    
    supplier = relationship('Supplier', back_populates='products')
