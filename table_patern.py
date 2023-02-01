from sqlalchemy.orm import declarative_base
from sqlalchemy import BLOB, FLOAT,TEXT, INTEGER, Column, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship


BaseClass = declarative_base()

class RowTableProduct(BaseClass):
    __tablename__ = 'Products'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    name = Column(TEXT)
    description = Column(TEXT)
    picture = Column(TEXT)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

    orders = relationship("RowTableOrderProduct", back_populates = "product")

class RowTableOrder(BaseClass):
    __tablename__ = 'Orders'

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    id_user = Column(INTEGER)
    pickupPoint = Column(TEXT)
    dateTime = Column(INTEGER)
    typePay = Column(TEXT)
    status = Column(TEXT)

    products = relationship("RowTableOrderProduct", back_populates = "order")

class RowTableOrderProduct(BaseClass):
    __tablename__ = 'Orders-Products'

    id = Column(INTEGER, primary_key = True)
    id_order = Column(ForeignKey("Products.id"))
    id_product = Column(ForeignKey("Orders.id"))
    
    quantity = Column(INTEGER)

    order = relationship("RowTableOrder", back_populates="products")
    product = relationship("RowTableProduct", back_populates="orders")
    
# class RowTableUser(BaseClass):
#     __tablename__ = 'Users'

#     id_Telegram = Column(INTEGER, primary_key = True)
#     role = Column(TEXT)
#     name = Column(TEXT)
#     lastName = Column(TEXT)
    
# class RowTableRole(BaseClass):    
#     __tablename__ = 'Roles'

#     id = Column(INTEGER, primary_key = True, authoincrement = True)
#     name = Column(INTEGER)

# class RowTablePickupPoint(BaseClass):
#     __tablename__ = 'Pickup points'    

#     id  = Column(INTEGER, primary_ket = True, autoincement = True)
#     name = Column(TEXT)
#     coordinats = Column(FLOAT)