from sqlalchemy.orm import declarative_base
from sqlalchemy import BLOB, FLOAT,TEXT, INTEGER, Column, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

BaseClass = declarative_base()

class Product(BaseClass):
    __tablename__ = 'Products'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(TEXT)
    description = Column(TEXT)
    picture = Column(TEXT)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

    orders = relationship("OrderProduct", back_populates = "product")

class Order(BaseClass):
    __tablename__ = 'Orders'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    id_user = Column(INTEGER)
    pickupPoint = Column(TEXT)
    dateTime = Column(INTEGER)
    typePay = Column(TEXT)
    status = Column(TEXT)

    products = relationship("OrderProduct", back_populates = "order")

class OrderProduct(BaseClass):
    __tablename__ = 'Orders-Products'

    id = Column(INTEGER, primary_key = True)

    id_order = Column(ForeignKey("Orders.id"))
    id_product = Column(ForeignKey("Products.id"))
    
    quantity = Column(INTEGER)

    order = relationship("Order", back_populates="products")
    product = relationship("Product", back_populates="orders")
    
